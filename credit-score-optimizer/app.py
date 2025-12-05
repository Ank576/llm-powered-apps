import streamlit as st
import requests
import json
from typing import Dict, List

# Page configuration
st.set_page_config(
    page_title="Credit Score Optimizer",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
    .improvement-tip {
        background: #f0f2f6;
        padding: 15px;
        border-left: 4px solid #667eea;
        border-radius: 5px;
        margin: 10px 0;
    }
    .success-box {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        padding: 15px;
        border-radius: 5px;
        color: #155724;
    }
    .warning-box {
        background: #fff3cd;
        border: 1px solid #ffeea0;
        padding: 15px;
        border-radius: 5px;
        color: #856404;
    }
</style>
""", unsafe_allow_html=True)

# Title and intro
st.title("💸 Credit Score Optimizer")
st.markdown("### Educational Demo: Personalized Credit Improvement Tips")
st.markdown("""
This is an **educational simulation** demonstrating how LLM-powered apps can provide personalized 
financial advice. Enter your credit profile below to receive AI-generated tips for improving 
your creditworthiness.
""")

# Warning disclaimer
st.warning(
    "📄 **Disclaimer**: This is a demo app for educational purposes only. "
    "Consult actual banks and financial advisors for real credit assessment."
)

# Sidebar for inputs
with st.sidebar:
    st.header("📃 Your Credit Profile")
    
    cibil_score = st.slider(
        "CIBIL Score",
        min_value=300,
        max_value=900,
        value=650,
        step=10,
        help="Credit Information Bureau India Limited (CIBIL) score ranges from 300-900"
    )
    
    dti_ratio = st.slider(
        "Debt-to-Income Ratio (%)",
        min_value=0,
        max_value=100,
        value=30,
        step=5,
        help="Percentage of gross monthly income used for debt payments"
    )
    
    credit_age = st.selectbox(
        "Credit History Age",
        ["No History", "0-1 year", "1-3 years", "3-7 years", "7-15 years", "15+ years"],
        index=2
    )
    
    inquiries = st.slider(
        "Hard Inquiries (Last 12 Months)",
        min_value=0,
        max_value=10,
        value=1,
        help="Number of times lenders checked your credit"
    )
    
    public_records = st.selectbox(
        "Public Records",
        ["None", "1 Bankruptcy", "2+ Bankruptcies", "Judgments"],
        index=0
    )

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Profile Summary")
    st.metric("Current CIBIL Score", f"{cibil_score}", 
              delta=f"{cibil_score - 650}" if cibil_score != 650 else "baseline")
    st.metric("DTI Ratio", f"{dti_ratio}%")
    st.metric("Inquiries (12mo)", f"{inquiries}")

with col2:
    st.subheader("🏆 Bank Eligibility Status")
    
    # Calculate approval likelihood (simple logic for demo)
    approval_score = 0
    feedback = []
    
    if cibil_score >= 750:
        approval_score += 40
        feedback.append("✅ Excellent CIBIL score for bank loans")
    elif cibil_score >= 700:
        approval_score += 25
        feedback.append("⚠️ Good CIBIL score; room for improvement")
    elif cibil_score >= 650:
        approval_score += 10
        feedback.append("📄 Average score; work on improvement")
    else:
        approval_score += 0
        feedback.append("❌ Low score; significant improvement needed")
    
    if dti_ratio < 30:
        approval_score += 30
        feedback.append("✅ Healthy DTI ratio (< 30%)")
    elif dti_ratio < 40:
        approval_score += 15
        feedback.append("⚠️ Acceptable DTI ratio (< 40%)")
    else:
        approval_score += 0
        feedback.append("❌ High DTI ratio; reduce debt")
    
    if inquiries <= 1:
        approval_score += 15
    elif inquiries <= 3:
        approval_score += 5
    
    if public_records == "None":
        approval_score += 15
    
    # Display approval likelihood
    st.metric("Bank Approval Likelihood", f"{min(approval_score, 100)}%")
    
    for item in feedback:
        if "✅" in item:
            st.success(item)
        elif "❌" in item:
            st.error(item)
        else:
            st.info(item)

# Personalized tips section
st.subheader("💡 Personalized Improvement Tips")

tips = []

# Generate tips based on profile
if cibil_score < 700:
    tips.append({
        "title": "1. Register on CIBIL & Dispute Errors",
        "description": "Get a free credit report from CIBIL. Dispute any incorrect entries within 30 days.",
        "impact": "+20-50 points",
        "priority": "HIGH"
    })
    tips.append({
        "title": "2. Establish Payment History",
        "description": "Make timely payments for next 30 days. This is tracked immediately by credit bureaus.",
        "impact": "+30-100 points",
        "priority": "HIGH"
    })

if dti_ratio > 30:
    tips.append({
        "title": "3. Reduce Credit Utilization",
        "description": f"You're at {dti_ratio}%. Target <30% by paying down revolving credit or requesting credit limit increase.",
        "impact": "+25-45 points",
        "priority": "HIGH"
    })
    tips.append({
        "title": "4. Debt Consolidation Strategy",
        "description": "Consider consolidating high-interest debt into a single lower-rate loan per RBI guidelines.",
        "impact": "+15-30 points",
        "priority": "MEDIUM"
    })

if inquiries > 3:
    tips.append({
        "title": "5. Space Your Credit Applications",
        "description": "You have {inquiries} inquiries. RBI recommends <3 per 12 months. Space applications 6+ months apart.",
        "impact": "Avoid -10 points",
        "priority": "MEDIUM"
    })

if credit_age == "No History":
    tips.append({
        "title": "6. Build Credit History",
        "description": "Start with a secured credit card or small personal loan. Build a 12-month clean payment record.",
        "impact": "+50-100 points (6-12 months)",
        "priority": "HIGH"
    })

if public_records != "None":
    tips.append({
        "title": "7. Address Legal Issues",
        "description": "Work with a legal advisor to resolve bankruptcy or judgment records. They can take 7-10 years to clear.",
        "impact": "Gradual improvement",
        "priority": "HIGH"
    })

# Default general tips
if len(tips) < 5:
    tips.append({
        "title": "8. Monitor Your Credit Report",
        "description": "Check your CIBIL report quarterly (free) at cibil.com. Report unauthorized inquiries immediately.",
        "impact": "Preventative",
        "priority": "MEDIUM"
    })
    tips.append({
        "title": "9. Diversify Credit Mix",
        "description": "Having credit cards + loans improves score. Aim for 3-4 active accounts per RBI best practices.",
        "impact": "+15-25 points",
        "priority": "MEDIUM"
    })

# Display tips in columns
for idx, tip in enumerate(tips[:6]):
    col1, col2 = st.columns([3, 1])
    with col1:
        color = "🗕" if tip["priority"] == "HIGH" else "📋"
        st.markdown(f"**{color} {tip['title']}**")
        st.markdown(tip["description"])
    with col2:
        st.markdown(f"**Impact**: {tip['impact']}")
        st.markdown(f"_Priority: {tip['priority']}_")
    st.divider()

# Projection section
st.subheader("📑 Timeline to Bank Eligibility")

if cibil_score < 700:
    timeline = [
        ("Month 1-2", "On-time payments established", "650 → 680"),
        ("Month 3-4", "Reduce DTI below 40%", "680 → 720"),
        ("Month 6", "Dispute errors resolved", "720 → 750"),
    ]
else:
    timeline = [
        ("Immediate", "You're eligible for most bank loans!", f"{cibil_score}"),
        ("Month 3", "Target 800+ for premium products", f"{cibil_score} → 800+"),
    ]

for stage, action, score_change in timeline:
    st.markdown(f"**{stage}**: {action} | {score_change}")
    st.progress(0.33 if stage.startswith("Month 1") else (0.66 if stage.startswith("Month 3") else 1.0))

# Disclaimer
st.markdown("---")
st.markdown("""
**Note**: This app provides general educational guidance based on RBI (Reserve Bank of India) credit norms. 
Actual credit decisions depend on individual bank policies. For real assessment, contact:
- **SBI Credit**: https://www.sbi.co.in/
- **HDFC Bank**: https://www.hdfcbank.com/
- **CIBIL Report**: https://www.cibil.com/
""")
