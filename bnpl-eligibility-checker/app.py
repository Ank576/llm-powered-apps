import streamlit as st
import json
from openai import OpenAI
import re

st.set_page_config(page_title="BNPL Checker", layout="centered", page_icon="🛒")
st.title("🛒 BNPL Eligibility Simulator")
st.caption("*AI-powered BNPL checker with RBI guidelines. Demo only.*")

with st.sidebar:
    st.header("User Profile")
    income = st.number_input("Annual Income (₹)", min_value=0.0, value=500000.0, step=10000.0)
    cibil = st.slider("CIBIL Score", 300, 900, 700)
    age = st.slider("Age", 18, 60, 28)

if st.button("🔍 Check Eligibility", type="primary", use_container_width=True):
    api_key = st.secrets.get("PERPLEXITY_API_KEY", None)
    if not api_key:
        st.error("⚠️ PERPLEXITY_API_KEY not found!")
        st.info("Add to Streamlit Secrets: PERPLEXITY_API_KEY = 'pplx-your-key'")
        st.stop()
    
    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")
    
    with st.spinner("Analyzing with RBI compliance..."):
        prompt = f"""You are a BNPL eligibility engine for India following RBI Digital Lending Guidelines.

Analyze this applicant:
- Age: {age}
- Annual Income: ₹{income:,.0f}
- CIBIL Score: {cibil}

Return ONLY valid JSON (no markdown, no code blocks):

{{
  "approved": boolean,
  "max_limit": number,
  "tenure_months": number,
  "interest_rate": "string",
  "citations": ["source1", "source2"],
  "reasoning": "string explanation"
}}

Rules: CIBIL ≥1500 for approval, income ≥3L for limits >25k, age 21-55 preferred."""

        try:
            response = client.chat.completions.create(
                model="sonar-pro",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            
            raw = response.choices[0].message.content.strip()
            raw = re.sub(r'``````', '', raw)
            
            json_match = re.search(r'\{.*\}', raw, re.DOTALL)
            if not json_match:
                st.error("No JSON found in response")
                st.code(raw)
                st.stop()
            
            json_str = json_match.group(0)
            result = json.loads(json_str)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Status", "✅ APPROVED" if result["approved"] else "❌ REJECTED", f"₹{result.get('max_limit', 0):,}")
            with col2:
                st.metric("Tenure", f"{result.get('tenure_months', 0)} months")
            
            st.json(result)
            
            with st.expander("📚 Citations"):
                for citation in result.get('citations', []):
                    st.write(f"- {citation}")
                    
        except json.JSONDecodeError as e:
            st.error(f"JSON parsing error: {e}")
        except Exception as e:
            st.error(f"API Error: {str(e)}")

st.markdown("---")
st.caption("**Disclaimer**: Demo only. Consult LazyPay/ZestMoney for real BNPL.")
