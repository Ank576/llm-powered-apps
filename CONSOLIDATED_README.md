# 🤖 LLM-Powered Fintech Apps Monorepo

**Collection of AI-powered financial applications** built with Streamlit & Perplexity LLM, designed for Indian financial compliance.

---

## 📂 Repository Structure

```
llm-powered-apps/
├── financial-goal-tracker/          # 💰 Investment Goal Planning
│   ├── app.py                       # Main Streamlit application
│   ├── requirements.txt             # Python dependencies
│   └── .python-version              # Python 3.11
│
├── bnpl-eligibility-checker/        # 🛒 Buy Now Pay Later Eligibility
│   ├── app.py                       # Main Streamlit application
│   ├── requirements.txt             # Python dependencies
│   └── .python-version              # Python 3.11
│
├── fair-practices-auditor/          # 🏦 RBI Fair Practices Auditor
│   ├── app.py                       # Main Streamlit application
│   ├── requirements.txt             # Python dependencies
│   └── .python-version              # Python 3.11
│
├── README.md                        # Main repository documentation
├── CONSOLIDATED_README.md           # This file
└── .python-version                  # Root Python version
```

---

## 🎯 Apps Overview

### 1. 💰 **Financial Goal Tracker**
**Location:** `financial-goal-tracker/`

AI-powered investment planning tool that generates personalized asset allocation recommendations.

**Features:**
- Multi-asset class analysis (Equity, Debt, Gold, Silver, Energy, Real Estate)
- Risk-adjusted portfolio recommendations
- Monthly SIP calculations
- Tax optimization (Section 80C, LTCG, STCG)
- Real-time market analysis via LLM
- Expected CAGR and confidence scoring

**Key Inputs:**
- Financial goal & target amount
- Current savings & investment tenure
- Risk appetite level
- Age, income & monthly capacity
- Investment preferences

**Output:**
- JSON response with asset allocation
- Monthly SIP recommendations
- Tax benefits & recommendations
- Market outlook 2025

---

### 2. 🛒 **BNPL Eligibility Checker**
**Location:** `bnpl-eligibility-checker/`

Simulates BNPL (Buy Now Pay Later) eligibility assessment following RBI Digital Lending Guidelines.

**Features:**
- CIBIL score-based eligibility
- Credit limit calculation
- Tenure recommendations (3-12 months)
- Interest rate estimation (0-18% APR)
- RBI guideline citations
- Approval/Rejection with reasoning

**Key Inputs:**
- Age (18-60)
- Annual Income (₹)
- CIBIL Score (300-900)

**Output:**
- Approval status
- Maximum credit limit
- Recommended tenure
- Interest rate range
- Regulatory citations

---

### 3. 🏦 **Fair Practices Auditor**
**Location:** `fair-practices-auditor/`

RBI-compliant loan terms auditor validating processing fees and prepayment penalties.

**Features:**
- Processing fee validation (≤1% of principal)
- Prepayment penalty audit (≤2% per annum)
- JSON-based compliance results
- RBI fair practices code citations
- APPROVE/REJECT/WARNING recommendations

**Key Inputs:**
- Loan principal amount
- Processing fee (%)
- Prepayment penalty (%)

**Output:**
- Compliance status
- Absolute fee amounts
- Violations detected
- Recommendations
- RBI references

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Streamlit
- Perplexity API key

### Local Setup

```bash
# Clone repository
git clone https://github.com/Ank576/llm-powered-apps.git
cd llm-powered-apps

# Install dependencies (shared)
pip install -r requirements.txt

# Or per-app:
cd financial-goal-tracker
pip install -r requirements.txt
```

### Get API Key
1. Visit [Perplexity API Dashboard](https://www.perplexity.ai/settings/api)
2. Generate API key
3. Store securely

### Run Apps

```bash
# Financial Goal Tracker
streamlit run financial-goal-tracker/app.py

# BNPL Eligibility Checker
streamlit run bnpl-eligibility-checker/app.py

# Fair Practices Auditor
streamlit run fair-practices-auditor/app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

**Step 1:** Fork repository → Sign up at [share.streamlit.io](https://share.streamlit.io)

**Step 2:** Create new app
- Repository: Your fork
- Main file: `<app-folder>/app.py`

**Step 3:** Add Secrets
```toml
PERPLEXITY_API_KEY = "pplx-your-key-here"
```

**Deployment Links:**
| App | URL | Status |
|-----|-----|--------|
| Financial Goal Tracker | [TBD] | 🟢 Active |
| BNPL Eligibility Checker | [TBD] | 🟢 Active |
| Fair Practices Auditor | [TBD] | 🟢 Active |

---

## 🔑 Environment Setup

### Local Development

Create `.streamlit/secrets.toml`:
```toml
PERPLEXITY_API_KEY = "pplx-your-key-here"
```

### Streamlit Cloud

App Settings → Secrets:
```
PERPLEXITY_API_KEY = pplx-your-key-here
```

---

## 📊 Technology Stack

| Component | Technology | Version |
|-----------|-----------|--------|
| **Frontend** | Streamlit | 1.38.0 |
| **LLM API** | Perplexity (sonar-pro) | Latest |
| **SDK** | OpenAI SDK | 1.12.0 |
| **HTTP** | httpx | 0.27.0 |
| **Runtime** | Python | 3.11.0 |

---

## 📋 API Response Examples

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
  "reasoning": "CIBIL ≥650, Income qualifies"
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

## ✅ Compliance & Regulations

### RBI Guidelines
- ✅ Fair Practices Code for loan terms
- ✅ Digital Lending Guidelines
- ✅ CIBIL score thresholds
- ✅ Interest rate regulations

### SEBI Compliance
- ✅ Investment recommendations
- ✅ Risk disclosures
- ✅ Tax implications
- ✅ Portfolio rebalancing guidance

---

## ⚠️ Disclaimers

**Educational Purpose:** These applications are for educational/demonstration purposes only.

**Not Financial Advice:** Consult SEBI-registered financial advisors before investing.

**Data Security:** No personal data is stored. API keys must be kept confidential.

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Open Pull Request

---

## 📚 Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [Perplexity API Docs](https://docs.perplexity.ai)
- [RBI Official Website](https://www.rbi.org.in)
- [SEBI Guidelines](https://www.sebi.gov.in)

---

## 📧 Contact

- **Author:** Ankit Saxena
- **GitHub:** [@Ank576](https://github.com/Ank576)
- **Portfolio:** [GitHub Projects](https://github.com/Ank576?tab=repositories)

---

## 📄 License

MIT License - See LICENSE file for details

---

**Built with 🧡 by Ankit Saxena**  
*AI-Powered Financial Tools for Modern India*

Last Updated: December 2025
