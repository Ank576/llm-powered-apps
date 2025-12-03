# 💳 BNPL Eligibility Checker

**RBI-Compliant Buy Now Pay Later Eligibility Assessment Engine**

An intelligent LLM-powered application that instantly evaluates customer eligibility for BNPL financing based on RBI Digital Lending Guidelines, CIBIL scores, and lending regulations.

## 🔗 Demo Link
- [CLICK HERE](https://bnpl-eligibility-checker-mev79gc9pmstrszvhsmufx.streamlit.app/)

## ✨ Features

- **CIBIL Score-Based Eligibility** - Instant eligibility determination (threshold ≥1500)
- **Dynamic Credit Limit Calculation** - Personalized lending limits based on credit profile
- **RBI Digital Lending Guidelines Compliance** - Full adherence to lending regulations
- **Tenure Recommendations** - Optimal 3-12 month repayment periods
- **Interest Rate Estimation** - 0-18% APR range with dynamic pricing
- **Income Verification Integration** - Basic income assessment
- **Approve/Reject/Warning Recommendations** - Clear decision with reasoning

## 🎯 Use Cases

- **E-commerce Platforms** - Instant BNPL eligibility at checkout
- **Fintech Applications** - Rapid customer onboarding and credit assessment
- **Lender Networks** - Quick credit decisioning for loan approvals
- **Financial Advisory** - Consumer creditworthiness evaluation
- **Compliance Testing** - Verify RBI guideline adherence

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

1. **Input Customer Data** - CIBIL score, income, requested amount
2. **Verification Check** - Age, income, and basic eligibility validation
3. **LLM Analysis** - Perplexity's sonar-pro evaluates against RBI guidelines
4. **Credit Decision** - Generate structured approval decision
5. **Display Results** - Show limit, tenure, interest rate, and reasoning

## 💡 Sample Input & Output

### Input
```json
{
  "cibil_score": 650,
  "monthly_income": 50000,
  "age": 28,
  "employment_type": "Salaried",
  "requested_amount": 15000
}
```

### Output
```json
{
  "approved": true,
  "max_limit": 50000,
  "recommended_tenure_months": 6,
  "interest_rate": "12-18% APR",
  "reasoning": "CIBIL ≥1500, Income qualifies for requested amount",
  "dynamic_limit": 50000
}
```

## 🔍 Compliance Standards

- **RBI Digital Lending Guidelines 2022** - Master circular on lending
- **CIBIL Score Validation** - Minimum score 1500 for eligibility
- **Income Assessment** - Debt-to-income ratio calculation
- **Age Requirements** - 21-60 years for BNPL eligibility
- **Documentation Standards** - KYC and income verification compliance

## 🤖 LLM Integration

Powered by **Perplexity's sonar-pro** model for:
- Multi-factor credit decision reasoning
- RBI regulation compliance verification
- Dynamic lending limit calculation
- Structured JSON credit decisions

## ⚖️ Disclaimer

**Educational Purpose Only** - This application is for demonstration and educational purposes. It is not financial advice. Always conduct proper KYC, income verification, and consult credit experts for actual lending decisions. This tool does not replace official credit scoring agencies.

## 📚 Resources

- [RBI Digital Lending Guidelines](https://www.rbi.org.in/)
- [CIBIL Score Information](https://www.cibil.com/)
- [RBI Master Circular on Lending](https://www.rbi.org.in/Scripts/NotificationUser.aspx)
- [BNPL Regulations](https://www.rbi.org.in/)


## 📝 License

MIT License - See main repository for details

## 👤 Author

Ankit Saxena - [GitHub](https://github.com/Ank576) | [Portfolio](https://github.com/Ank576)
