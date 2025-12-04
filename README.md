# 🤖 LLM-Powered Apps

[![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-red?style=flat&logo=streamlit)](https://streamlit.io/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue?style=flat&logo=python)](https://www.python.org/)
[![Perplexity LLM](https://img.shields.io/badge/Perplexity%20LLM-sonar--pro-purple?style=flat)](https://www.perplexity.ai/)
[![RBI/SEBI Compliant](https://img.shields.io/badge/RBI%2FSEBI-Compliant-green?style=flat)](https://www.rbi.org.in/)

**AI-Powered Fintech Applications Suite** built with Streamlit and Perplexity LLM. A collection of regulatory-compliant tools for Indian financial operations.

---

## 💪 What's Inside?

This monorepo contains **4 production-ready LLM applications** designed for modern financial operations:

### 1. **💰 [Financial Goal Tracker](./financial-goal-tracker)**

**Smart investment planning with AI-powered asset allocation**

- 🏸 Multi-asset class analysis (Equity, Debt, Gold, Silver, Crude Oil, Real Estate)
- 🎩 Risk-adjusted portfolio recommendations
- 📊 Monthly SIP calculations with confidence scoring
- 📸 Tax optimization (Section 80C, LTCG, STCG compliance)
- 🎯 Real-time market analysis via LLM
- 🗐️ Expected CAGR & alternative strategies

**Use Cases:** Retirement planning, Education fund, Home purchase, Wealth creation

---

### 2. **🛒 [BNPL Eligibility Checker](./bnpl-eligibility-checker)**

**RBI-compliant Buy Now Pay Later eligibility assessment engine**

- ✅ CIBIL score-based instant eligibility (threshold ≥1500)
- 🎯 Dynamic credit limit calculation
- 📅 Tenure recommendations (3-12 months)
- 💵 Interest rate estimation (0-18% APR range)
- 📇 RBI Digital Lending Guidelines citations
- 🎯 Approve/Reject/Warning recommendations with reasoning

**Compliance:** RBI Digital Lending Guidelines, Income verification, Age eligibility

---

### 3. **🏦 [Fair Practices Auditor](./fair-practices-auditor)**

**RBI Fair Practices Code compliance validator for loan terms**

- ✅ Processing fee audit (≤1% of principal)
- ✅ Prepayment penalty validation (≤2% per annum)
- 📊 JSON-based compliance results
- 📇 RBI Fair Practices Code citations
- 🎯 APPROVE/REJECT/WARNING with violations
- 🗐️ Fee breakdown and absolute amounts

**Rules:** RBI Circular on Fair Practices Code, Penalty guidelines

---

### 4. 🏦 [Loan Against Asset Checker](./loan-against-asset-checker)

**RBI-compliant collateral valuation and LTV-based loan assessment**

- 💰 Gold loan validation (LTV ≤75%, purity ≥99.5%)
- 🏠 Property mortgage assessment (LTV ≤80%, value estimation)
- 📈 Share collateral analysis (LTV ≤50%, SEBI compliance)
- 🤖 LLM-powered valuation & market insights
- 📋 Real-time LTV calculations & approval status
- ✅ Regulatory compliance documentation

**Rules:** RBI Master Circular on Gold Loans, Property Valuation Guidelines, SEBI Share Pledge Norms



## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Streamlit 1.38.0+
- Perplexity API key (free tier available)

### Installation

```bash
# Clone repository
git clone https://github.com/Ank576/llm-powered-apps.git
cd llm-powered-apps

# Install dependencies
pip install -r requirements.txt

# Get Perplexity API key
# Visit: https://www.perplexity.ai/settings/api
```

### Run Individual Apps

```bash
# Financial Goal Tracker
streamlit run financial-goal-tracker/app.py

# BNPL Eligibility Checker
streamlit run bnpl-eligibility-checker/app.py

# Fair Practices Auditor
streamlit run fair-practices-auditor/app.py
```

---

## 📊 Technology Stack

| Technology | Purpose | Version |
|-----------|---------|----------|
| **Streamlit** | Web Framework | 1.38.0 |
| **Perplexity LLM** | AI Engine | sonar-pro |
| **OpenAI SDK** | API Integration | 1.12.0 |
| **Python** | Runtime | 3.11+ |
| **httpx** | HTTP Client | 0.27.0 |

---

## 🌐 Deployment

### Streamlit Cloud (Recommended)

```bash
# 1. Fork this repository
# 2. Sign up at share.streamlit.io
# 3. Create new app for each folder
# 4. Add secrets:
PERPLEXITY_API_KEY = "pplx-your-key-here"
```

**Deployment Links (Coming Soon):**
- Financial Goal Tracker: [TBD]
- BNPL Eligibility Checker: [TBD]
- Fair Practices Auditor: [TBD]

---

## 📋 Folder Structure

```
llm-powered-apps/
├── financial-goal-tracker/
│   ├── app.py                 # Main Streamlit app
│   ├── requirements.txt       # Dependencies
│   └── README.md              # Documentation
│
├── bnpl-eligibility-checker/
│   ├── app.py                 # Main Streamlit app
│   ├── requirements.txt       # Dependencies
│   └── README.md              # Documentation
│
├── fair-practices-auditor/
│   ├── app.py                 # Main Streamlit app
│   ├── requirements.txt       # Dependencies
│   └── README.md              # Documentation
│
├── CONSOLIDATED_README.md # Full technical guide
├── README.md              # This file
└── .gitignore             # Git config
```

---

## ✅ Compliance & Regulations

### RBI Guidelines
- ✅ **Fair Practices Code** for loan terms
- ✅ **Digital Lending Guidelines** 2022
- ✅ **CIBIL score** thresholds & validation
- ✅ **Interest rate** regulatory caps

### SEBI Guidelines
- ✅ **Investment recommendations** disclosures
- ✅ **Risk** appropriateness
- ✅ **Tax implications** clarity
- ✅ **Portfolio rebalancing** guidance

---

## 🤖 LLM Integration

All apps use **Perplexity's sonar-pro model** for:
- Real-time market data access
- Regulatory compliance verification
- Multi-step financial reasoning
- JSON-structured output generation
- RBI/SEBI guideline citations

---

## 📊 Sample Outputs

### Financial Goal Tracker
```json
{
  "goal_achievable": true,
  "confidence_score": "85",
  "required_monthly_sip": 25000,
  "expected_return_cagr": "10-12%",
  "asset_allocation": {
    "equity": {"percentage": 60, "allocation_amount": 15000},
    "debt": {"percentage": 25, "allocation_amount": 6250},
    "gold": {"percentage": 10, "allocation_amount": 2500}
  }
}
```

### BNPL Checker
```json
{
  "approved": true,
  "max_limit": 50000,
  "tenure_months": 6,
  "interest_rate": "0-18% APR",
  "reasoning": "CIBIL ≥1500, Income qualifies for limit"
}
```

### Fair Practices Auditor
```json
{
  "is_compliant": true,
  "recommendation": "APPROVE",
  "processing_fee_compliant": true,
  "prepayment_penalty_compliant": true,
  "violations": []
}
```

---

## 📚 Documentation

- **[CONSOLIDATED_README.md](./CONSOLIDATED_README.md)** - Complete technical guide (310+ lines)
- **[financial-goal-tracker/README.md](./financial-goal-tracker/README.md)** - App-specific docs
- **[bnpl-eligibility-checker/README.md](./bnpl-eligibility-checker/README.md)** - App-specific docs
- **[fair-practices-auditor/README.md](./fair-practices-auditor/README.md)** - App-specific docs

---

## 🔗 Links & Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Perplexity API Docs](https://docs.perplexity.ai)
- [RBI Official Guidelines](https://www.rbi.org.in)
- [SEBI Regulations](https://www.sebi.gov.in)

---

## 🚀 Stay Tuned for More Apps!

**Upcoming in Pipeline:**
- 🏦 **Home Loan Pre-Qualifier** - RBI-compliant mortgage eligibility
- 📕 **Insurance Coverage Analyzer** - IRDA-compliant policy matcher
- 💳 **UPI Transaction Auditor** - NPCI compliance checker
- 📊 **Portfolio Rebalancer** - Tax-loss harvesting optimizer
- 📋 **Debt Consolidation Planner** - Loan optimization tool
- 💰 **Micro-Investment Assistant** - SIP strategy builder

**Want a specific financial app?** [Open an issue](https://github.com/Ank576/llm-powered-apps/issues) or contribute!

---

## ⚠️ Disclaimer

**Educational & Demo Purpose:** These applications are for demonstration and educational purposes only. They are not financial advice.

**Not Actual Financial Advisory:** Always consult SEBI-registered financial advisors before making investment decisions.

**Data Security:** No personal data is stored. Keep your Perplexity API key confidential.

**Regulatory Compliance:** While built with RBI/SEBI guidelines, always verify with official sources.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Open a Pull Request

---

## 📄 License

MIT License - See [LICENSE](./LICENSE) file for details

---

## 📧 Contact & Support

- **Author:** Ankit Saxena
- **GitHub:** [@Ank576](https://github.com/Ank576)
- **Portfolio:** [Ank576 Projects](https://github.com/Ank576?tab=repositories)
- **Email:** [GitHub Profile](https://github.com/Ank576)

---

## ⭐ Show Your Support

If you find this project useful, please **⭐ Star** this repository!

---

**Built with 🧡 by Ankit Saxena**  
*AI-Powered Financial Tools for Modern India*  
*December 2025*
