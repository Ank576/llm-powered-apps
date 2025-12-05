# 📈 Value Stock Finder

**Educational stock screening application** that identifies potentially undervalued stocks using fundamental financial metrics. Built with Streamlit and yfinance.

---

## 💫 Overview

Value Stock Finder helps discover stocks trading below intrinsic value using:

- **Graham Number** - Benjamin Graham's intrinsic value formula
- **Valuation Metrics** - P/E, P/B, P/S ratios
- **Profitability** - ROE, ROA analysis
- **Financial Health** - Debt-to-Equity assessment
- **Valuation Score** - 0-100 scoring system

---

## ✨ Key Features

### Graham Number Valuation
- Calculates intrinsic value: `√(22.5 × EPS × Book Value)`
- Shows discount/premium to fair value
- Estimates upside potential

### Personalized Filters
- Max P/E Ratio (lower = cheaper)
- Minimum ROE (higher = better quality)
- Maximum Debt-to-Equity (lower = safer)

### Valuation Scoring
- **70+** = Undervalued (✅ Strong Buy Signal)
- **50-70** = Fair Value (⚠️ Hold/Review)
- **<50** = Overvalued (❌ Avoid)

### Metrics Dashboard
- P/E Ratio, P/B Ratio, P/S Ratio
- ROE, ROA, Debt-to-Equity
- Real-time insights vs criteria

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/ank576/llm-powered-apps.git
cd llm-powered-apps/value-stock-finder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
streamlit run app.py
```

---

## 📄 How to Use

1. Enter NSE stock ticker (e.g., RELIANCE.NS, TCS.NS)
2. Adjust filters (P/E, ROE, D/E ratios)
3. Click "Analyze Stock"
4. Review valuation metrics and insights

---

## 💡 Investment Concepts

### Graham Number
```
Graham Number = √(22.5 × EPS × Book Value Per Share)
```

- If Price < Graham Number → Potentially undervalued
- If Price > Graham Number → Potentially overvalued

### Key Ratios

| Metric | Ideal | Lower is Better? |
|--------|-------|------------------|
| P/E | 15-25 | Yes |
| P/B | <1.5 | Yes |
| P/S | <3 | Yes |
| ROE | >15% | No (Higher) |
| ROA | >10% | No (Higher) |
| D/E | <1 | Yes |

---

## 📊 Tech Stack

- **Streamlit** 1.38.0 - UI framework
- **yfinance** 0.2.32 - Stock data
- **pandas, numpy** - Data processing
- **Python** 3.9+

---

## 📖 Educational Value

1. Fundamental Analysis
2. Valuation Methods
3. Risk Assessment
4. Streamlit Development
5. Stock Market Basics

---

## ⚠️ Disclaimer

> **EDUCATIONAL DEMO ONLY**
>
> - NOT real financial advice
> - FOR LEARNING PURPOSES ONLY
> - Always consult financial advisors
> - Do your own research (DYOR)

---

## 🔗 Resources

- [Yahoo Finance](https://finance.yahoo.com)
- [NSE Website](https://www.nseindia.com)
- [Graham Number](https://en.wikipedia.org/wiki/Graham_number)
- [Streamlit Docs](https://docs.streamlit.io)

---

**Status**: ✅ Active Development | **Author**: Ank576
