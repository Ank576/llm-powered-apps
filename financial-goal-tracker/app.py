import streamlit as st
import json
from openai import OpenAI
import re

st.set_page_config(page_title="Financial Goal Tracker", layout="wide", page_icon="💰")

st.title("💰 AI-Powered Financial Goal Tracker")
st.markdown("Get personalized investment recommendations across multiple asset classes using AI.")

with st.sidebar:
    st.header("📊 Your Financial Profile")
    
    goal_name = st.text_input("Goal Name", value="Retirement Fund", placeholder="e.g., Child Education, Home Purchase")
    target_amount = st.number_input("Target Amount (₹)", min_value=10000.0, value=5000000.0, step=50000.0, format="%.0f")
    current_savings = st.number_input("Current Savings (₹)", min_value=0.0, value=500000.0, step=10000.0, format="%.0f")
    tenure_years = st.slider("Investment Tenure (Years)", 1, 30, 10)
    
    st.markdown("---")
    
    st.subheader("Risk Appetite")
    risk_appetite = st.select_slider(
        "Select your risk tolerance",
        options=["Very Conservative", "Conservative", "Moderate", "Aggressive", "Very Aggressive"],
        value="Moderate"
    )
    
    age = st.slider("Age", 18, 65, 30)
    monthly_income = st.number_input("Monthly Income (₹)", min_value=10000.0, value=100000.0, step=5000.0, format="%.0f")
    monthly_investment = st.number_input("Monthly Investment Capacity (₹)", min_value=1000.0, value=20000.0, step=1000.0, format="%.0f")
    
    st.markdown("---")
    
    st.subheader("Preferences")
    prefer_liquid = st.checkbox("Prefer liquid investments", value=True)
    include_real_estate = st.checkbox("Include Real Estate", value=False)
    tax_saving = st.checkbox("Prioritize tax-saving instruments", value=True)

gap_amount = max(0, target_amount - current_savings)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Target Amount", f"₹{target_amount:,.0f}")
with col2:
    st.metric("Current Savings", f"₹{current_savings:,.0f}")
with col3:
    st.metric("Gap to Cover", f"₹{gap_amount:,.0f}", delta=f"{(gap_amount/target_amount*100):.1f}%")
with col4:
    st.metric("Tenure", f"{tenure_years} years")

st.markdown("---")

if st.button("🔍 Generate Investment Plan", type="primary", use_container_width=True):
    api_key = st.secrets.get("PERPLEXITY_API_KEY", None)
    if not api_key:
        st.error("⚠️ PERPLEXITY_API_KEY not found in Streamlit secrets!")
        st.info("Setup: In Streamlit Cloud → Settings → Secrets, add: PERPLEXITY_API_KEY = 'pplx-your-key-here'")
        st.stop()
    
    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")
    
    with st.spinner("🤖 Analyzing your profile and market conditions..."):
        prompt = f"""You are a SEBI-registered financial advisor specializing in goal-based wealth planning for Indian investors.

INVESTOR PROFILE:
- Goal: {goal_name}
- Target Amount: ₹{target_amount:,.0f}
- Current Savings: ₹{current_savings:,.0f}
- Gap Amount: ₹{gap_amount:,.0f}
- Investment Tenure: {tenure_years} years
- Risk Appetite: {risk_appetite}
- Age: {age} years
- Monthly Income: ₹{monthly_income:,.0f}
- Monthly Investment Capacity: ₹{monthly_investment:,.0f}
- Liquidity Preference: {"High" if prefer_liquid else "Medium"}
- Real Estate Interest: {"Yes" if include_real_estate else "No"}
- Tax Saving Priority: {"Yes" if tax_saving else "No"}

Return ONLY valid JSON (no markdown, no code blocks):

{{
  "goal_achievable": boolean,
  "confidence_score": "number 0-100",
  "required_monthly_sip": number,
  "expected_corpus": number,
  "expected_return_cagr": "string percentage",
  "asset_allocation": {{
    "equity": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "debt": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "gold": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "silver": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "crude_energy": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "real_estate": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}}
  }},
  "recommendations": ["recommendation1", "recommendation2"],
  "risk_factors": ["risk1", "risk2"],
  "tax_benefits": ["benefit1", "benefit2"],
  "rebalancing_frequency": "string",
  "alternative_strategies": ["strategy1", "strategy2"],
  "market_outlook_2025": "string summary",
  "disclaimer": "string"
}}"""
        try:
            response = client.chat.completions.create(
                model="sonar-pro",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )
            
            raw = response.choices[0].message.content.strip()
            match = re.search(r"\{.*\}", raw, re.DOTALL)
            if not match:
                st.error("LLM did not return JSON.")
                st.code(raw)
                st.stop()
            
            json_str = match.group(0)
            result = json.loads(json_str)
            
            st.success("✅ Investment plan generated!")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Goal Achievable", "✅ YES" if result.get("goal_achievable") else "⚠️ CHECK")
            with col2:
                st.metric("Confidence", f"{result.get('confidence_score','0')}%")
            with col3:
                st.metric("Required Monthly SIP", f"₹{result.get('required_monthly_sip',0):,.0f}")
            with col4:
                st.metric("Expected CAGR", result.get("expected_return_cagr", "N/A"))
            
            st.markdown("---")
            st.subheader("📊 Asset Allocation Recommendation")
            
            allocation = result.get("asset_allocation", {})
            colA, colB = st.columns(2)
            
            with colA:
                st.markdown("### Allocation Breakdown")
                for asset, details in allocation.items():
                    pct = details.get("percentage", 0)
                    amt = details.get("allocation_amount", 0)
                    if pct > 0:
                        st.markdown(f"**{asset.replace('_', ' ').title()}**: {pct}% (₹{amt:,.0f}/month)")
            
            with colB:
                st.markdown("### Suggested Instruments")
                for asset, details in allocation.items():
                    instruments = details.get("instruments", [])
                    if instruments:
                        st.markdown(f"**{asset.replace('_', ' ').title()}**")
                        for inst in instruments:
                            st.write(f"-  {inst}")
            
            with st.expander("🔍 Full JSON Response"):
                st.json(result)
            
            st.markdown("---")
            st.warning(result.get("disclaimer", "Educational purposes only."))
            
        except json.JSONDecodeError as e:
            st.error(f"JSON parsing error: {e}")
        except Exception as e:
            st.error(f"API Error: {e}")

st.markdown("---")
st.caption("Built with 🧡 by Ankit Saxena | AI-powered financial planning")
