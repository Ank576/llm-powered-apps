import streamlit as st
import json
from openai import OpenAI
import re

st.set_page_config(page_title="RBI Fair Practices Auditor", layout="centered", page_icon="🏦")
st.title("🏦 RBI Fair Practices Auditor")
st.markdown("Enter loan terms to check compliance with RBI fair practices code.")

with st.sidebar:
    st.header("Loan Terms")
    principal = st.number_input("Loan Principal (₹)", min_value=0.0, value=100000.0, step=1000.0, format="%.0f")
    processing_fee_pct = st.number_input("Processing Fee (%)", min_value=0.0, max_value=10.0, value=0.50, step=0.1, format="%.2f")
    prepayment_penalty_pct = st.number_input("Prepayment Penalty (%)", min_value=0.0, max_value=10.0, value=1.00, step=0.1, format="%.2f")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Principal", f"₹{principal:,.0f}")
with col2:
    st.metric("Processing Fee", f"{processing_fee_pct}%")
with col3:
    st.metric("Prepayment Penalty", f"{prepayment_penalty_pct}%")

st.markdown("---")

if st.button("🔍 Audit Loan Terms", type="primary", use_container_width=True):
    api_key = st.secrets.get("PERPLEXITY_API_KEY", None)
    if not api_key:
        st.error("⚠️ PERPLEXITY_API_KEY not found!")
        st.info("Setup: In Streamlit Cloud → Settings → Secrets: PERPLEXITY_API_KEY = 'pplx-your-key'")
        st.stop()
    
    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")
    
    with st.spinner("📏 Checking RBI compliance..."):
        prompt = f"""You are an RBI Fair Practices Code compliance auditor for loan terms.

Analyze these loan terms:
- Principal: ₹{principal:,.0f}
- Processing Fee: {processing_fee_pct}%
- Prepayment Penalty: {prepayment_penalty_pct}%

RBI Fair Practices Code Rules:
- Processing fee must be ≤1% of principal
- Prepayment penalty must be ≤2% per annum

Return ONLY valid JSON (no markdown, no code blocks):

{{
  "is_compliant": boolean,
  "recommendation": "APPROVE|REJECT|WARNING",
  "processing_fee_compliant": boolean,
  "prepayment_penalty_compliant": boolean,
  "processing_fee_absolute": number,
  "violations": ["reason1", "reason2"],
  "citations": ["RBI source1"],
  "reasoning": "string explanation"
}}"""

        try:
            response = client.chat.completions.create(
                model="sonar-pro",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            
            raw = response.choices[0].message.content.strip()
            match = re.search(r'\{.*\}', raw, re.DOTALL)
            if not match:
                st.error("No JSON found")
                st.stop()
            
            result = json.loads(match.group(0))
            
            st.subheader("Audit Results")
            col1, col2 = st.columns(2)
            
            with col1:
                fee_status = "✅ Compliant" if result["processing_fee_compliant"] else "❌ Non-compliant (>1%)")
                st.metric("Processing Fee", f"₹{result.get('processing_fee_absolute', 0):,.0f}", f"{processing_fee_pct}%")
                if result["processing_fee_compliant"]:
                    st.success(fee_status)
                else:
                    st.error(fee_status)
            
            with col2:
                penalty_status = "✅ Compliant" if result["prepayment_penalty_compliant"] else "❌ Non-compliant (>2%)")
                st.metric("Prepayment Penalty", f"{prepayment_penalty_pct}%")
                if result["prepayment_penalty_compliant"]:
                    st.success(penalty_status)
                else:
                    st.error(penalty_status)
            
            if result["is_compliant"]:
                st.success("🎉 Loan terms approved!")
            else:
                st.error("🚫 Loan terms rejected")
                for violation in result.get("violations", []):
                    st.warning(f"⚠️ {violation}")
            
            st.json(result)
            
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.caption("Built with 🧡 by Ankit Saxena")
