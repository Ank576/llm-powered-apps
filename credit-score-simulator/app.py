import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Credit Score Simulator",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💳 Credit Score Simulator")
st.markdown("**AI-Powered Credit Score Impact Analyzer**")

with st.sidebar:
    st.header("📊 Credit Profile")
    current_score = st.slider("Current Credit Score", 300, 900, 700, step=10)
    
    st.subheader("Payment Behavior")
    payment_history = st.slider("Payment History (months of perfect payment)", 0, 120, 36)
    late_payments = st.number_input("Number of late payments (last 2 years)", 0, 10, 0)
    
    st.subheader("Credit Utilization")
    total_credit = st.number_input("Total Credit Limit (Rs)", 0, 10000000, 500000, step=50000)
    current_balance = st.number_input("Current Balance (Rs)", 0, total_credit if total_credit > 0 else 1000000, 150000, step=10000)
    utilization = (current_balance / total_credit * 100) if total_credit > 0 else 0
    
    st.subheader("Recent Inquiries")
    recent_inquiries = st.slider("Hard inquiries (last 6 months)", 0, 10, 1)
    new_accounts = st.slider("New accounts opened (last 12 months)", 0, 5, 0)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Score", current_score)

with col2:
    st.metric("Credit Utilization", f"{utilization:.1f}%")

with col3:
    st.metric("Late Payments", late_payments)

st.divider()

st.subheader("📈 Score Impact Analysis")

tab1, tab2, tab3 = st.tabs(["Impact Factors", "Scenario Planning", "Recommendations"])

with tab1:
    st.write("**Positive Factors:**")
    col1, col2 = st.columns(2)
    with col1:
        if payment_history >= 24:
            st.success(f"✓ Strong payment history: {payment_history} months")
        if utilization < 30:
            st.success(f"✓ Low credit utilization: {utilization:.1f}%")
    
    with col2:
        if late_payments == 0:
            st.success("✓ No late payments")
        if recent_inquiries <= 2:
            st.success(f"✓ Reasonable inquiries: {recent_inquiries}")
    
    st.write("**Areas for Improvement:**")
    col1, col2 = st.columns(2)
    with col1:
        if utilization > 50:
            st.warning(f"⚠ High utilization: {utilization:.1f}% (reduce to <30%)")
        if recent_inquiries > 3:
            st.warning(f"⚠ Multiple inquiries: {recent_inquiries} (limit new credit applications)")
    
    with col2:
        if late_payments > 0:
            st.warning(f"⚠ Late payments detected: {late_payments}")
        if new_accounts >= 2:
            st.warning(f"⚠ Recent new accounts: {new_accounts}")

with tab2:
    st.write("Scenario Planning: Simulate different actions and their impact")
    scenario_col1, scenario_col2 = st.columns(2)
    
    with scenario_col1:
        st.write("**Scenario 1: Reduce Utilization**")
        new_utilization = st.slider("Target Utilization %", 0, 100, int(max(30, utilization - 20)))
        expected_gain_1 = min(50, (utilization - new_utilization) * 2)
        st.info(f"Expected score gain: +{expected_gain_1:.0f} points")
    
    with scenario_col2:
        st.write("**Scenario 2: Maintain Perfect Payment**")
        months_perfect = st.slider("Months of perfect payment", 0, 36, 12)
        expected_gain_2 = min(100, months_perfect * 2.5)
        st.info(f"Expected score gain: +{expected_gain_2:.0f} points")

with tab3:
    st.write("**Personalized Recommendations:**")
    recommendations = []
    
    if utilization > 30:
        recommendations.append(f"1. Pay down credit cards to reduce utilization below 30% (currently {utilization:.1f}%)")
    
    if late_payments > 0:
        recommendations.append("2. Prioritize paying all bills on time - this is the most important factor")
    
    if recent_inquiries > 3:
        recommendations.append("3. Avoid applying for new credit in the near future")
    
    if payment_history < 24:
        recommendations.append(f"4. Build payment history - maintain consistent on-time payments (currently {payment_history} months)")
    
    if not recommendations:
        st.success("✓ Your credit profile looks great! Continue maintaining good habits.")
    else:
        for rec in recommendations:
            st.write(rec)

st.divider()
st.info("⚠️ **Disclaimer:** This tool is for educational purposes only. Actual credit scores are calculated by credit bureaus using proprietary algorithms. For official credit assessment, contact your bank or authorized financial institution.")
