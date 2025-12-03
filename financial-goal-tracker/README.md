# 💰 Financial Goal Tracker

**Smart Investment Planning with AI-Powered Asset Allocation**

An intelligent LLM-powered financial planning application that helps users achieve their investment goals through personalized, risk-adjusted asset allocation strategies. Powered by Perplexity LLM and built for compliance with SEBI investment guidelines.

## ✨ Features

- **Multi-Asset Class Analysis** - Equity, Debt, Gold, Silver, Crude Oil, Real Estate allocation
- **Risk-Adjusted Portfolio Recommendations** - Personalized recommendations based on risk profile
- **Monthly SIP Calculations** - Smart Systematic Investment Plans with confidence scoring
- **Tax Optimization** - Section 80C, LTCG, STCG compliance features
- **Real-Time Market Analysis** - LLM-powered market insights via Perplexity
- **Expected CAGR Predictions** - 10-12% realistic returns based on asset mix
- **Alternative Strategies** - Multiple portfolio options for different goals

## 🎯 Use Cases

- **Retirement Planning** - Build corpus for post-retirement income
- **Education Fund** - Plan for child's educational expenses
- **Home Purchase** - Accumulate down payment for property
- **Wealth Creation** - Long-term wealth accumulation strategies
- **Debt Management** - Balanced investment vs debt repayment

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

## 📊 How It Works

1. **Input Financial Goal** - Amount needed, timeline, and current savings
2. **Risk Assessment** - User's risk tolerance and investment experience
3. **LLM Analysis** - Perplexity evaluates market conditions and recommends allocation
4. **Generate Plan** - Personalized asset allocation and SIP calculation
5. **Tax Planning** - Optimize for tax efficiency and compliance
6. **View Projections** - Expected returns and alternative scenarios

## 💡 Sample Input & Output

### Input
```json
{
  "goal_amount": 2500000,
  "timeline_years": 5,
  "current_savings": 500000,
  "risk_profile": "Moderate",
  "monthly_capacity": 25000
}
```

### Output
```json
{
  "goal_achievable": true,
  "confidence_score": "85%",
  "required_monthly_sip": 25000,
  "expected_return_cagr": "10-12%",
  "asset_allocation": {
    "equity": {"percentage": 60, "allocation_amount": 1500000},
    "debt": {"percentage": 25, "allocation_amount": 625000},
    "gold": {"percentage": 10, "allocation_amount": 250000},
    "real_estate": {"percentage": 5, "allocation_amount": 125000}
  },
  "tax_implications": "LTCG applicable after 1 year"
}
```

## 🔍 Compliance Standards

- **SEBI Guidelines for Portfolio Management** - Adherence to regulatory standards
- **Section 80C Tax Benefits** - ELSS, PPF, FD coverage
- **LTCG/STCG Optimization** - Long-term vs short-term capital gains
- **Risk Profiling** - Know Your Customer (KYC) compliance
- **Suitability Analysis** - Recommendations based on investor profile

## 🤖 LLM Integration

Powered by **Perplexity's sonar-pro** model for:
- Multi-asset class correlation analysis
- Real-time market sentiment assessment
- Tax-efficient portfolio construction
- Alternative scenario generation
- CAGR projection and reasoning

## ⚖️ Disclaimer

**Educational Purpose Only** - This application is for demonstration and educational purposes. It is NOT financial advice. Always consult with SEBI-registered investment advisors before making investment decisions. Past performance doesn't guarantee future results. Market conditions change rapidly.

## 📚 Resources

- [SEBI Investment Guidelines](https://www.sebi.gov.in/)
- [SEBI Portfolio Management Guidelines](https://www.sebi.gov.in/regulations)
- [Income Tax Section 80C Benefits](https://www.incometax.gov.in/)
- [Asset Allocation Strategy Guide](https://www.sebi.gov.in/)
- [Tax Optimization for Investments](https://www.incometax.gov.in/)

## 🔗 Demo Link

**Coming Soon** - The app will be deployed on Streamlit Cloud

## 📝 License

MIT License - See main repository for details

## 👤 Author

Ankit Saxena - [GitHub](https://github.com/Ank576) | [Portfolio](https://github.com/Ank576)
