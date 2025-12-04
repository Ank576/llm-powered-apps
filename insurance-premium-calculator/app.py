import streamlit as st
import os
from typing import Dict, Any

import httpx

PPLX_API_KEY = os.getenv("PERPLEXITY_API_KEY", "")
PPLX_MODEL = "sonar-pro"


def call_llm(prompt: str) -> Dict[str, Any]:
    if not PPLX_API_KEY:
        raise RuntimeError("PERPLEXITY_API_KEY not set. Please add it in your environment or Streamlit secrets.")

    headers = {
        "Authorization": f"Bearer {PPLX_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": PPLX_MODEL,
        "temperature": 0.2,
        "max_tokens": 800,
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "insurance_premium_response",
                "schema": {
                    "type": "object",
                    "properties": {
                        "is_eligible": {"type": "boolean"},
                        "recommended_products": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "type": {"type": "string"},
                                    "coverage_amount": {"type": "number"},
                                    "annual_premium": {"type": "number"},
                                    "monthly_premium": {"type": "number"},
                                    "key_features": {"type": "array", "items": {"type": "string"}},
                                    "notes": {"type": "string"}
                                },
                                "required": [
                                    "type",
                                    "coverage_amount",
                                    "annual_premium",
                                    "monthly_premium",
                                    "key_features"
                                ]
                            }
                        },
                        "tax_benefits": {
                            "type": "object",
                            "properties": {
                                "section_80d_deduction": {"type": "number"},
                                "section_80c_deduction": {"type": "number"},
                                "notes": {"type": "string"}
                            },
                            "required": ["section_80d_deduction"]
                        },
                        "risk_summary": {"type": "string"},
                        "irda_compliance_notes": {"type": "string"}
                    },
                    "required": [
                        "is_eligible",
                        "recommended_products",
                        "tax_benefits",
                        "risk_summary",
                        "irda_compliance_notes"
                    ]
                }
            }
        },
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an Indian insurance expert helping estimate IRDA-compliant premiums "
                    "for term, life, and health insurance. You must not give guaranteed numbers, "
                    "only indicative estimates for educational purposes. Always include clear disclaimers "
                    "and highlight that customers must consult IRDA-registered insurers or agents."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    }

    with httpx.Client(timeout=60) as client:
        resp = client.post("https://api.perplexity.ai/chat/completions", headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()

    try:
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        raise RuntimeError(f"Unexpected LLM response format: {e}")


def build_prompt(form_values: Dict[str, Any]) -> str:
    return f"""
Act as an IRDA-aware insurance planner for India.

User profile:
- Age: {form_values['age']}
- Gender: {form_values['gender']}
- City type: {form_values['city_type']}
- Annual income: INR {form_values['annual_income']}
- Existing health conditions: {form_values['health_conditions']}
- Lifestyle factors: {', '.join(form_values['lifestyle_factors']) if form_values['lifestyle_factors'] else 'None reported'}
- Smoker: {form_values['smoker_status']}
- Family coverage: {form_values['family_coverage']}
- Number of dependents: {form_values['dependents']}
- Desired coverage amount (life/term): INR {form_values['desired_life_coverage']}
- Desired coverage amount (health): INR {form_values['desired_health_coverage']}

Task:
1. Suggest suitable mix of term, life, and health insurance products for this profile.
2. For each suggested product, provide an estimated coverage amount, annual premium, monthly premium, and 3-5 key features.
3. Compute indicative tax benefit under Section 80D (health) and Section 80C (life/term where relevant). Assume current limits for an individual and family in India.
4. Provide a concise risk summary for the profile.
5. Add IRDA compliance notes, including: need for proposal form, medical underwriting, KYC, free-look period, and that actual premiums vary by insurer.
6. Ensure all output follows the JSON schema shared and uses INR amounts.

Do not ask the user questions. Fill the JSON directly.
    """.strip()


def main() -> None:
    st.set_page_config(
        page_title="IRDA-Compliant Insurance Premium Estimator",
        page_icon="💡",
        layout="centered",
    )

    st.title("🛡️ IRDA-Compliant Insurance Premium Estimator")
    st.write(
        "Indicative premium estimation for life, term, and health insurance in India. "
        "Created with 🧡 by Ankit Saxena. For educational purposes only. Not a substitute for advice from IRDA-registered entities."
    )

    with st.sidebar:
        st.header("User Profile")
        age = st.number_input("Age", min_value=18, max_value=75, value=30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        city_type = st.selectbox("City Type", ["Metro", "Non-Metro"])
        annual_income = st.number_input("Annual Income (INR)", min_value=100000, max_value=100000000, value=1000000, step=50000)

        health_conditions = st.text_area(
            "Existing health conditions",
            help="E.g., diabetes, hypertension, heart disease, none",
        ) or "None"

        lifestyle_factors = st.multiselect(
            "Lifestyle factors",
            ["Sedentary", "Moderate exercise", "Regular exercise", "High stress job", "Alcohol consumption"],
        )

        smoker_status = st.selectbox("Smoker status", ["Non-smoker", "Occasional smoker", "Regular smoker"])

        family_coverage = st.selectbox(
            "Family coverage",
            ["Self only", "Self + Spouse", "Self + Spouse + Children", "Family including parents"],
        )

        dependents = st.number_input("Number of dependents", min_value=0, max_value=10, value=2)

        desired_life_coverage = st.number_input(
            "Desired life/term coverage (INR)", min_value=500000, max_value=100000000, value=10000000, step=500000
        )
        desired_health_coverage = st.number_input(
            "Desired health coverage (INR)", min_value=200000, max_value=5000000, value=1000000, step=100000
        )

        submit = st.button("Estimate Premiums", type="primary")

    if submit:
        if not PPLX_API_KEY:
            st.error("PERPLEXITY_API_KEY not found. Please configure it in your environment or Streamlit secrets.")
            return

        form_values = {
            "age": age,
            "gender": gender,
            "city_type": city_type,
            "annual_income": annual_income,
            "health_conditions": health_conditions,
            "lifestyle_factors": lifestyle_factors,
            "smoker_status": smoker_status,
            "family_coverage": family_coverage,
            "dependents": dependents,
            "desired_life_coverage": desired_life_coverage,
            "desired_health_coverage": desired_health_coverage,
        }

        prompt = build_prompt(form_values)

        with st.spinner("Contacting insurance planning assistant..."):
            try:
                result = call_llm(prompt)
            except Exception as e:
                st.error(f"Error while calling LLM: {e}")
                return

        st.subheader("Premium Estimates & Recommendations")

        if result.get("risk_summary"):
            st.markdown("### Risk Summary")
            st.write(result["risk_summary"])

        if result.get("recommended_products"):
            st.markdown("### Recommended Products")
            for idx, prod in enumerate(result["recommended_products"], start=1):
                with st.expander(f"{idx}. {prod['type']} - Indicative Premium"):
                    st.write(f"**Coverage amount:** ₹{prod['coverage_amount']:,.0f}")
                    st.write(f"**Annual premium (approx):** ₹{prod['annual_premium']:,.0f}")
                    st.write(f"**Monthly premium (approx):** ₹{prod['monthly_premium']:,.0f}")

                    st.write("**Key features:**")
                    for f in prod.get("key_features", []):
                        st.write(f"- {f}")

                    if prod.get("notes"):
                        st.write("**Notes:**")
                        st.write(prod["notes"])

        tax = result.get("tax_benefits", {})
        st.markdown("### Indicative Tax Benefits")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Section 80D (Health)", f"₹{tax.get('section_80d_deduction', 0):,.0f}")
        with col2:
            st.metric("Section 80C (Life/Term)", f"₹{tax.get('section_80c_deduction', 0):,.0f}")

        if tax.get("notes"):
            st.write(tax["notes"])

        if result.get("irda_compliance_notes"):
            st.markdown("### IRDA & Regulatory Notes")
            st.write(result["irda_compliance_notes"])

        st.info(
            "This tool is build by Ankit Saxena which provides indicative estimates for learning and planning only. "
            "Actual premiums, terms, and benefits depend on the insurer's underwriting policies, "
            "medical tests, disclosures in the proposal form, and IRDA regulations."
        )


if __name__ == "__main__":
    main()
