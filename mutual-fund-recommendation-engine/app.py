import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title="Mutual Fund Recommendation Engine",
    page_icon="💱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💱 Mutual Fund Recommendation Engine")
st.markdown("**SEBI-Compliant AI-Powered Mutual Fund Analyzer**")

# Initialize session state
if 'risk_profile' not in st.session_state:
    st.session_state.risk_profile = "Moderate"
if 'investment_amount' not in st.session_state:
    st.session_state.investment_amount = 100000

with st.sidebar:
    st.header("📌 Investment Profile")
    
    risk_appetite = st.selectbox(
        "Risk Appetite",
        ["Conservative", "Moderate", "Aggressive"],
        index=1
    )
    
    investment_horizon = st.slider(
        "Investment Horizon (Years)",
        min_value=1,
        max_value=40,
        value=7,
        step=1
    )
    
    financial_goal = st.selectbox(
        "Primary Financial Goal",
        ["Retirement", "Education", "Home Purchase", "Wealth Creation"],
        index=3
    )
    
    investment_amount = st.number_input(
        "Investment Amount (Rs)",
        min_value=10000,
        value=100000,
        step=10000
    )
    
    st.markdown("---")
    st.subheader("⚠️ Disclaimer")
    st.info("This tool is for educational purposes. Not investment advice.")

st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Risk Profile", risk_appetite)
with col2:
    st.metric("Horizon", f"{investment_horizon} yrs")
with col3:
    st.metric("Goal", financial_goal.split()[0])
with col4:
    st.metric("Investment", f"Rs {investment_amount/100000:.1f}L")

st.divider()

st.subheader("📈 Fund Recommendations")

# Sample fund data based on risk profile
fund_data = {
    "Conservative": [
        {"name": "Axis Liquid Fund", "type": "Liquid", "return": "5.2%", "expense": "0.35%"},
        {"name": "HDFC Short Term Debt", "type": "Debt", "return": "6.8%", "expense": "0.45%"},
        {"name": "ICICI Prudential Fixed Maturity", "type": "Debt", "return": "7.1%", "expense": "0.40%"},
        {"name": "Aditya Birla Sun Life Money Manager", "type": "Money Market", "return": "5.5%", "expense": "0.38%"},
        {"name": "Mirae Asset Government Securities", "type": "G-Sec", "return": "6.5%", "expense": "0.25%"},
    ],
    "Moderate": [
        {"name": "ICICI Prudential Balanced Advantage", "type": "Balanced", "return": "10.2%", "expense": "0.65%"},
        {"name": "Axis Equity Hybrid Fund", "type": "Hybrid", "return": "9.8%", "expense": "0.72%"},
        {"name": "HDFC Hybrid Equity Fund", "type": "Hybrid", "return": "10.5%", "expense": "0.70%"},
        {"name": "Motilal Oswal Midcap Fund", "type": "Equity", "return": "15.2%", "expense": "0.95%"},
        {"name": "Kotak Flexicap Fund", "type": "Equity", "return": "14.8%", "expense": "0.85%"},
    ],
    "Aggressive": [
        {"name": "DSP Focused Growth Fund", "type": "Large Cap", "return": "16.2%", "expense": "0.82%"},
        {"name": "ICICI Prudential Multi-Asset Fund", "type": "Multi Asset", "return": "12.5%", "expense": "0.75%"},
        {"name": "Canara Robeco Emerging Equities", "type": "Mid Cap", "return": "18.5%", "expense": "1.05%"},
        {"name": "Sundaram Small Cap Fund", "type": "Small Cap", "return": "19.2%", "expense": "1.15%"},
        {"name": "Axis Focused 25 Fund", "type": "Large Cap", "return": "17.8%", "expense": "0.88%"},
    ]
}

recommendations = fund_data[risk_appetite]

tab1, tab2, tab3 = st.tabs(["Top Recommendations", "Comparison", "Analysis"])

with tab1:
    for idx, fund in enumerate(recommendations, 1):
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.write(f"**{idx}. {fund['name']}**")
            st.caption(f"Type: {fund['type']}")
        with col2:
            st.metric("1Y Return", fund["return"])
        with col3:
            st.metric("Expense", fund["expense"])
        st.divider()

with tab2:
    df = pd.DataFrame(recommendations)
    st.dataframe(df, use_container_width=True, hide_index=True)

with tab3:
    st.write("### Fund Selection Rationale")
    st.markdown(f"""
    Based on your profile:
    - **Risk Appetite:** {risk_appetite}
    - **Time Horizon:** {investment_horizon} years
    - **Goal:** {financial_goal}
    - **Investment:** Rs {investment_amount:,}
    
    The recommended funds align with your risk profile and investment timeline.
    """)

st.divider()
st.warning(
    "**⚠️ SEBI Compliance Notice:** This tool provides recommendations for educational purposes only. "
    "It is not investment advice. Consult with SEBI-registered financial advisors before investing. "
    "Past performance does not guarantee future results."
)
