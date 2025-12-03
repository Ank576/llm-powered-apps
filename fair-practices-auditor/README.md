# 🏦 Fair Practices Auditor

**RBI Fair Practices Code Compliance Validator for Loan Terms**

An intelligent LLM-powered application that audits loan agreements against RBI's Fair Practices Code standards, ensuring compliance and protecting borrower interests.

## ✨ Features

- **Processing Fee Audit** - Validates processing fees don't exceed 1% of principal
- **Prepayment Penalty Validation** - Ensures penalties comply with RBI limits (≤2% per annum)
- **JSON-Based Compliance Results** - Structured audit findings with recommendations
- **RBI Fair Practices Code Citations** - Direct references to applicable guidelines
- **Multi-Violation Detection** - Identifies APPROVE/REJECT/WARNING status with detailed reasoning
- **Fee Breakdown Analysis** - Comprehensive fee structure examination

## 🎯 Use Cases

- **Borrower Protection** - Verify loan terms before accepting
- **Bank Compliance** - Validate loan documentation against RBI standards
- **Legal Review** - Quick compliance audit for loan agreements
- **Consumer Advocacy** - Check if terms violate fair practices

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

1. **Input Loan Terms** - Enter processing fees, prepayment penalties, and loan amount
2. **LLM Analysis** - Perplexity's sonar-pro model evaluates against RBI guidelines
3. **Compliance Check** - System validates each component
4. **Generate Report** - Structured JSON output with APPROVE/REJECT/WARNING status
5. **View Results** - See detailed reasoning and specific violations

## 💡 Sample Input & Output

### Input
```json
{
  "principal_amount": 500000,
  "processing_fee": 6000,
  "prepayment_penalty": 12000,
  "loan_tenure_months": 60
}
```

### Output
```json
{
  "is_compliant": true,
  "recommendation": "APPROVE",
  "processing_fee_compliant": true,
  "prepayment_penalty_compliant": true,
  "violations": [],
  "fee_breakdown": {
    "processing_fee_percentage": "1.2%",
    "penalty_per_annum": "0.48%"
  }
}
```

## 🔍 Compliance Standards

- **RBI Circular on Fair Practices Code** - Master circular on lending operations
- **Processing Fee Limits** - ≤1% of loan amount for MSME, ≤2% for others
- **Prepayment Penalty** - ≤2% per annum for floating rate, ≤4% for fixed rate
- **Documentation Requirements** - All fees must be disclosed upfront

## 🤖 LLM Integration

Powered by **Perplexity's sonar-pro** model for:
- Multi-step RBI regulation reasoning
- Regulatory compliance verification
- Fee calculation validation
- Structured JSON output generation

## ⚖️ Disclaimer

**Educational Purpose Only** - This application is for demonstration and educational purposes. It is not legal advice. Always consult with qualified legal professionals and registered financial advisors for loan agreement review and compliance matters.

## 📚 Resources

- [RBI Fair Practices Code](https://www.rbi.org.in/)
- [RBI Circular on Lending](https://www.rbi.org.in/Scripts/NotificationUser.aspx)
- [Loan Agreement Standards](https://www.rbi.org.in/)

## 🔗 Demo Link

**Coming Soon** - The app will be deployed on Streamlit Cloud

## 📝 License

MIT License - See main repository for details

## 👤 Author

Ankit Saxena - [GitHub](https://github.com/Ank576) | [Portfolio](https://github.com/Ank576)
