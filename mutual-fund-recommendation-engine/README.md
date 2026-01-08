# 💱 Mutual Fund Recommendation Engine

**SEBI-Compliant AI-Powered Mutual Fund Analyzer**

An intelligent Streamlit application that uses LLMs to recommend mutual funds based on risk appetite, investment horizon, and financial goals. Leverages RAG techniques for prospectus analysis and SEBI-compliant investment recommendations.

## 📖 Overview

Mutual Fund Recommendation Engine is a comprehensive investment advisory tool designed to help Indian investors find suitable mutual funds aligned with their financial profile. It analyzes fund characteristics, risk metrics, and historical performance while maintaining strict SEBI compliance.

**Version:** 1.0.0 | **Status:** Active Development | **Updated:** January 2026

---

## ✨ Key Features

- **Risk-Based Fund Matching**: Automatically recommends funds matching your risk appetite (Conservative, Moderate, Aggressive)
- **Goal-Oriented Analysis**: Aligns fund recommendations with specific financial goals (Retirement, Education, Home, Wealth)
- **Investment Horizon Consideration**: Factors in time frame (Short <3yr, Medium 3-7yr, Long >7yr) for fund selection
- **RAG-Powered Prospectus Analysis**: Uses Retrieval-Augmented Generation for detailed fund document analysis
- **SEBI Compliance**: Adheres to SEBI guidelines on fund recommendations and disclosures
- **Performance Metrics Dashboard**: Historical returns, volatility, Sharpe ratio, and expense ratios
- **Portfolio Diversification Suggestions**: Recommendations for portfolio construction and asset allocation
- **Fund Comparison Tools**: Side-by-side comparison of recommended funds

---

## 🏗️ Technical Architecture

**Tech Stack:**
- Frontend: Streamlit 1.28.1
- LLM: Perplexity API with RAG
- Data Processing: Pandas 2.0.3, NumPy 1.24.3
- PDF Processing: PyPDF2 (for prospectus analysis)
- Backend: Python 3.11+
- Compliance: SEBI Guidelines

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip package manager
- SEBI-compliant database/API access (optional)

### Installation

```bash
git clone https://github.com/Ank576/llm-powered-apps.git
cd llm-powered-apps/mutual-fund-recommendation-engine
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

Open browser to `http://localhost:8501`

---

## 📊 How It Works

### Input Parameters

**Investment Profile:**
- Risk Appetite (Conservative/Moderate/Aggressive)
- Investment Horizon (years)
- Financial Goal (Retirement, Education, Home, Wealth Creation)
- Available Investment Amount (Rs)

**Preferences:**
- Fund Category Preferences
- Geographic Focus (India/Global)
- Tax Considerations

### Analysis Engine

1. **Risk Assessment** - Evaluates investor profile
2. **Fund Screening** - Filters eligible funds based on criteria
3. **Prospectus Analysis** - RAG-powered document analysis
4. **Performance Evaluation** - Historical metrics comparison
5. **Diversification Check** - Portfolio construction suggestions
6. **Recommendations** - Ranked fund suggestions with reasoning

### Output

- **Top 5 Fund Recommendations** with scores
- **Fund Comparison Matrix** (Returns, Risk, Expense Ratio, NAV)
- **Portfolio Allocation Suggestions**
- **Risk-Return Trade-off Analysis**
- **Tax Implications Report**

---

## 🔐 SEBI Compliance

**Mandatory Disclaimers:**
- Not a substitute for professional investment advice
- Past performance is not indicative of future results
- Investor should review fund prospectus before investing
- Recommendations based on historical data and current conditions

**Regulatory Adherence:**
- Follows SEBI Mutual Funds Regulations (MFR)
- Complies with SEBI FPI regulations
- Adheres to Fair Practices Code
- Maintains data privacy per SEBI standards

---

## 👨‍💻 Developer Information

**Created by:** Ankit Saxena  
**Email:** ankit.saxena76@nmims.edu.in  
**GitHub:** [@Ank576](https://github.com/Ank576)  
**Location:** Jhansi, Uttar Pradesh, India  

---

## ⚠️ DISCLAIMER

**IMPORTANT:** This tool is for **EDUCATIONAL AND DEMONSTRATION PURPOSES ONLY**.

It does NOT:
- Constitute investment advice
- Replace professional financial advisory
- Guarantee returns or risk assessment accuracy
- Override regulatory requirements

Always consult with SEBI-registered investment advisors before making investment decisions.

---

## 📄 License

MIT License - See [LICENSE](../LICENSE) file

---

## 📧 Contact

- **Email:** ankit.saxena76@nmims.edu.in
- **GitHub:** [@Ank576](https://github.com/Ank576)
- **Repository:** [llm-powered-apps](https://github.com/Ank576/llm-powered-apps)

**Last Updated:** January 8, 2026 | 5:00 PM IST
