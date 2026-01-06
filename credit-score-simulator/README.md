# 💳 Credit Score Simulator

**AI-Powered Credit Score Impact Analyzer**

An intelligent Streamlit application that simulates and predicts credit score changes based on financial behaviors. Helps users understand how their actions impact creditworthiness per RBI guidelines.

## 📖 Overview

Credit Score Simulator is a comprehensive financial education tool for understanding credit scoring dynamics in India. Provides real-time simulations of how financial behaviors affect credit scores.

**Version:** 1.0.0 | **Status:** Active Development | **Updated:** January 2026

---

## ✨ Key Features

- **Score Impact Simulation**: Real-time visualization of how payment history, credit utilization, and inquiries affect your score
- **Behavioral Analysis**: AI-powered insights using Perplexity LLM on financial decisions
- **Scenario Planning**: Compare multiple financial scenarios and their credit impacts side-by-side
- **RBI Compliance**: Aligned with RBI guidelines on credit assessment and fair lending practices
- **Interactive Dashboard**: Real-time visualization with intuitive interface
- **Personalized Recommendations**: Actionable advice based on your specific credit profile

---

## 🏗️ Technical Architecture

**Tech Stack:**
- Frontend: Streamlit 1.28.1
- LLM: Perplexity API
- Backend: Python 3.11+
- Data Processing: Pandas 2.0.3, NumPy 1.24.3
- Compliance: RBI Guidelines

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip package manager
- Virtual environment (recommended)

### Installation

```bash
git clone https://github.com/Ank576/llm-powered-apps.git
cd llm-powered-apps/credit-score-simulator
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

**Credit Profile:**
- Current Credit Score (300-900)
- Total Credit Limit (in Rs)
- Current Balance (in Rs)

**Payment Behavior:**
- Payment History (months of perfect payment)
- Late Payments (last 2 years)

**Recent Activity:**
- Hard Inquiries (last 6 months)
- New Accounts Opened (last 12 months)

### Credit Score Weightage

- Payment History: 35%
- Credit Utilization: 30%
- Credit History Length: 15%
- Credit Mix: 10%
- New Inquiries: 10%

---

## 📋 Features Breakdown

### Tab 1: Impact Factors
Analyzes your credit profile:
- Positive financial behavior factors
- Areas needing improvement
- Score improvement opportunities

### Tab 2: Scenario Planning
Simulate two scenarios:
1. Reduce Utilization - Impact of paying down credit cards
2. Perfect Payment - Benefits of maintaining perfect payments

### Tab 3: Recommendations
Personalized advice:
- Specific utilization reduction targets
- Payment priority strategies
- Credit application timeline
- Credit history building steps

---

## 🔐 Compliance & Regulations

**RBI Guidelines Adherence:**
- Digital Lending Norms (NBFC)
- Credit Information Companies (CIC) Guidelines
- Fair Lending Practices Code
- Data Privacy & Aadhaar Act Compliance

---

## 👨‍💻 Developer Information

**Created by:** Ankit Saxena  
**Email:** ankit.saxena76@nmims.edu.in  
**GitHub:** [@Ank576](https://github.com/Ank576)  
**Location:** Jhansi, Uttar Pradesh, India  

**Background:**
- Aspiring Product Manager (Fintech Focus)
- AI/LLM Application Developer
- Stock Market Analysis Enthusiast
- Deep expertise in Indian Financial Ecosystem

**Related Projects:**
- [Financial Goal Tracker](https://github.com/Ank576/llm-powered-apps/tree/main/financial-goal-tracker)
- [BNPL Eligibility Checker](https://github.com/Ank576/llm-powered-apps/tree/main/bnpl-eligibility-checker)
- [Fair Practices Auditor](https://github.com/Ank576/llm-powered-apps/tree/main/fair-practices-auditor)
- [Insurance Premium Calculator](https://github.com/Ank576/llm-powered-apps/tree/main/insurance-premium-calculator)

---

## 📚 Usage Examples

**Young Professional** (35% utilization, no late payments)
- Current Score: 750+ | Recommendation: Maintain habits, diversify credit mix

**New Borrower** (Limited history)
- Current Score: 600-650 | Recommendation: Build history, maintain low utilization

**Improving Credit** (High utilization, previous late payments)
- Current Score: 550-650 | Recommendation: Reduce utilization <30%, maintain 6+ months perfect payment

---

## 🔗 Deployment

**Local Development:**
```bash
streamlit run app.py
```

**Streamlit Cloud:**
Ready for deployment to Streamlit Cloud

---

## 📞 Support

- **Issues:** Check [GitHub Issues](https://github.com/Ank576/llm-powered-apps/issues)
- **Contributions:** Fork → Feature Branch → Pull Request

---

## ⚠️ DISCLAIMER

**IMPORTANT:** This tool is for **EDUCATIONAL & DEMONSTRATION PURPOSES ONLY**.

It does NOT:
- Replace professional financial advice
- Replace official credit scores by authorized agencies (CIBIL, Equifax, Experian, CRIF High Mark)
- Guarantee credit approval or specific limits
- Substitute for registered financial advisor guidance

For official credit assessment, always contact your bank or authorized financial institution.

---

## 📄 License

MIT License - See [LICENSE](../LICENSE) file

---

## 🙏 Acknowledgments

- RBI for credit guidelines and regulatory framework
- Perplexity AI for LLM capabilities
- Streamlit team for the framework
- NMIMS for educational support

---

## 📈 Future Roadmap

- [ ] Integration with actual CIBIL API
- [ ] Multi-language support (Hindi, Regional)
- [ ] Mobile app version
- [ ] Advanced ML models for prediction
- [ ] Bank API integration
- [ ] Historical score tracking
- [ ] Export reports to PDF

---

## 📧 Contact

- **Email:** ankit.saxena76@nmims.edu.in
- **GitHub:** [@Ank576](https://github.com/Ank576)
- **Repository:** [llm-powered-apps](https://github.com/Ank576/llm-powered-apps)

**Last Updated:** January 7, 2026 | 2:30 AM IST
