# 💸 Credit Score Optimizer

**Educational LLM-powered fintech application** built with Streamlit and Perplexity API. Demonstrates personalized credit improvement tips based on user financial profiles and RBI (Reserve Bank of India) credit guidelines.

---

## 📋 Overview

This demo app showcases how LLM (Large Language Models) can power fintech applications for financial wellness. Users input their credit profile details and receive:

- 🏆 **Bank Eligibility Assessment** - Real-time approval likelihood calculation
- 💡 **Personalized Tips** - AI-generated credit improvement strategies
- 📊 **Interactive Dashboard** - Visual profile analysis and metrics
- 📈 **Timeline Projection** - Estimated milestones to bank loan eligibility
- 📄 **RBI Compliance** - Guidelines based on Reserve Bank of India credit norms

---

## ✨ Features

### Input Profile (Sidebar)
- **CIBIL Score**: 300-900 range slider
- **Debt-to-Income Ratio**: 0-100% slider
- **Credit History Age**: Dropdown selection
- **Hard Inquiries**: 0-10 range slider (last 12 months)
- **Public Records**: None / Bankruptcy / Judgments selection

### Real-Time Analysis
- Bank approval likelihood calculation
- Credit profile summary metrics
- Eligibility feedback (✅ Good / ⚠️ Fair / ❌ Poor)
- Impact scoring for improvement opportunities

### Personalized Recommendations
Dynamic tip generation based on profile:
1. Register on CIBIL & Dispute Errors
2. Establish Payment History (30-day tracking)
3. Reduce Credit Utilization (<30% target)
4. Debt Consolidation Strategy
5. Space Credit Applications (RBI norms)
6. Build Credit History (secured cards)
7. Address Legal Issues
8. Monitor Credit Report Quarterly
9. Diversify Credit Mix

### Timeline & Progress
- Month-by-month eligibility progression
- Score improvement projections
- Milestone tracking
- Bank-ready threshold indicators

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip or conda

### Installation

```bash
# Clone the repository
git clone https://github.com/ank576/llm-powered-apps.git
cd llm-powered-apps/credit-score-optimizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📊 Tech Stack

| Component | Technology | Version |
|-----------|-----------|----------|
| **Frontend** | Streamlit | 1.38.0 |
| **Language** | Python | 3.9+ |
| **Data Processing** | pandas, numpy | 2.1.4, 1.24.3 |
| **LLM Integration** | Perplexity API | 0.2.0 |
| **Optional Viz** | Plotly | 5.17.0 |
| **Testing** | pytest | 7.4.3 |

---

## 📚 Educational Use Cases

This app demonstrates:

1. **LLM Prompting** - Dynamic prompt engineering based on user inputs
2. **Streamlit UI/UX** - Interactive components and real-time state management
3. **Financial Logic** - Credit scoring algorithms (simplified for demo)
4. **RBI Compliance** - Credit bureau guidelines and regulatory norms
5. **Fintech Architecture** - User input → Analysis → Personalized Output

---

## 🔧 Future Enhancements

- [ ] Integration with real CIBIL API (requires authentication)
- [ ] LLM-powered dynamic tip generation via Perplexity API
- [ ] PDF report export with improvement action plan
- [ ] Multi-language support (Hindi, Regional languages)
- [ ] Loan calculator (home, auto, personal)
- [ ] Bank comparison tool (SBI vs HDFC vs ICICI rates)
- [ ] Credit card recommendation engine
- [ ] Mobile-responsive design

---

## 📖 How It Works

```
User Input (Sidebar)
      ↓
Profile Validation
      ↓
Approval Score Calculation (Rule-based)
      ↓
Tip Generation (Dynamic based on profile)
      ↓
Timeline Projection (Milestone-based)
      ↓
Displayed in Dashboard
```

---

## ⚖️ Disclaimer

> **This is an EDUCATIONAL DEMO only.**
> 
> - **Not a real credit assessment tool**
> - **For learning purposes only** - understand fintech app architecture
> - **Do not use for actual financial decisions**
> - Consult actual banks (SBI, HDFC, ICICI) for real credit assessment
> - All calculations are simplified and for demonstration only

---

## 🔗 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [CIBIL Credit Bureau](https://www.cibil.com/)
- [RBI Credit Information Guidelines](https://www.rbi.org.in/)
- [SBI Home Loans](https://www.sbi.co.in/)
- [HDFC Bank Credit Products](https://www.hdfcbank.com/)
- [Perplexity API Docs](https://docs.perplexity.ai/)

---

## 📝 License

MIT License - See LICENSE file for details

---

## 👤 Author

**Ank576** - [GitHub Profile](https://github.com/ank576)

Part of the **LLM-Powered Apps** collection for fintech and legal tech learning.

---

## 🤝 Contributing

Contributions welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📧 Contact & Support

For questions or suggestions:
- Open an issue on [GitHub Issues](https://github.com/ank576/llm-powered-apps/issues)
- Check existing documentation in repo
- Review other apps in the LLM-Powered Apps collection

---

**Last Updated**: December 2024
**Status**: ✅ Active Development
