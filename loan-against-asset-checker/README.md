# Loan Against Asset Checker

🏦 **AI-Powered RBI-Compliant Loan Eligibility Validator**

A professional Streamlit application for validating loan eligibility against asset values (Gold, Property, Shares) with real-time RBI compliance checks and LLM-powered legal analysis.

---

## 🎯 Features

✅ **Multi-Asset Support**
- Gold Loan validation with purity & location-based LTV
- Property Mortgage with circle rate compliance
- Share Pledge against NIFTY indices

✨ **Smart Validation Engine**
- Instant RBI rule enforcement (LTV ratios, asset minimums, loan caps)
- Real-time error detection with actionable fixes
- Interactive progress indicators and animations

🤖 **AI-Powered Legal Analysis**
- Powered by Perplexity LLM for latest RBI guidelines
- Comprehensive compliance breakdowns with citations
- Recommendations for applicants

🎨 **Professional UX**
- Responsive, interactive dashboard with smooth animations
- Consistent typography and visual hierarchy
- Built with ❤️ for fintech professionals

---

## 🚀 Live Demo

👉 **[Try the Live Streamlit App](https://loan-against-asset-checker-mxwjikgdchx2zogcmcy7av.streamlit.app/)**

No installation needed—click above to test it live!

---

## 📋 Installation

### Prerequisites
- Python 3.9+
- pip
- Perplexity API key (for LLM analysis)

### Setup

1. **Clone or navigate to this folder:**
   ```bash
   cd loan-against-asset-checker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variable:**
   ```bash
   export PERPLEXITY_API_KEY="your-api-key-here"
   ```

4. **Run the app:**
   ```bash
   streamlit run streamlit_app.py
   ```

5. Open your browser to `http://localhost:8501`

---

## 📁 Folder Structure

```
loan-against-asset-checker/
├── streamlit_app.py        # Main Streamlit application
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🔑 Key Features Breakdown

### 1. **Gold Loan Validation**
- Urban LTV: 75% | Rural LTV: 90%
- Minimum Purity: 18 carats
- Max Loan Amount: ₹20 lakhs

### 2. **Property Mortgage Validation**
- Standard LTV: 60%
- Max LTV: 70%
- Circle Rate must be ≥ 90% of property value

### 3. **Share Pledge Validation**
- NIFTY50 eligible indices
- LTV: 50%
- Real-time market compliance checks

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Python)
- **LLM:** Perplexity API (Sonar model)
- **Validation Engine:** Custom RBI rule interpreter
- **Deployment:** Streamlit Cloud

---

## 🔒 Security & Privacy

- No data is stored or logged
- All validations run locally
- API keys managed via environment variables
- Compliant with RBI data protection guidelines

---

## 📖 How to Use

1. **Select Asset Type** from sidebar (Gold/Property/Shares)
2. **Enter asset details** (value, loan amount, location, etc.)
3. **Click "Submit for Validation"** to run instant checks
4. **Review results** including:
   - Approval status (✅ APPROVED / ❌ REJECTED)
   - Max eligible loan amount
   - LTV utilization ratio
   - RBI compliance warnings
5. **Get AI insights** with detailed legal analysis and recommendations

---

## 👨‍💼 About

**Built by Ankit Saxena** with 🧡

Fintech product manager & AI enthusiast exploring RBI compliance automation and LLM-powered legal tech.

- 🔗 [GitHub Portfolio](https://github.com/Ank576)
- 💼 [Standard Chartered](https://www.standardchartered.com)

---

## 📝 License

MIT License - feel free to fork, modify, and use!

---

## 🤝 Feedback & Contributions

Have suggestions? Found a bug? Issues and PRs are welcome!

For questions or feedback, please open a GitHub issue on this repository.

---

**Powered by Streamlit & Perplexity AI** 🚀
