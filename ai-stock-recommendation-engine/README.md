# 🤖 AI-Powered Stock Recommendation Engine

## Overview

The **AI-Powered Stock Recommendation Engine** is an intelligent fintech application that leverages Large Language Models (LLM) and advanced market analysis to provide personalized buy/sell/hold recommendations for Indian stock market portfolios. It combines AI-powered insights from Perplexity with technical analysis to help investors optimize their portfolio allocations.

**Key Innovation:** Integrates Perplexity API for LLM-powered stock analysis alongside real-time NSE market data and technical indicators.

## Features

### 1. **5-Stock Portfolio Input**
- Accept up to 5 stock tickers with custom percentage allocations
- Validate that portfolio allocations sum to 100%
- Support for NSE stocks with .NS suffix (e.g., TCS.NS, INFY.NS)

### 2. **Personalized Buy/Sell/Hold Recommendations**
- AI-powered recommendations using Perplexity LLM
- Considers market conditions, company fundamentals, and technical indicators
- Real-time NSE price data via yfinance

### 3. **Portfolio Rebalancing (60/30/10 Model)**
- Large-Cap (60%): Blue-chip stocks for stability
- Mid-Cap (30%): Growth potential stocks
- Small-Cap (10%): High-risk/high-reward opportunities
- Suggests rebalancing weights based on allocation model

### 4. **Tax-Loss Harvesting Suggestions**
- Identifies underperforming stocks in the portfolio
- Suggests replacement stocks in similar sectors
- Helps optimize after-tax returns

### 5. **Sector Overlap Detection**
- Analyzes sector exposure in the portfolio
- Identifies concentration risks
- Recommends diversification improvements

### 6. **Underperforming Stock Identification**
- Tracks RSI (Relative Strength Index) for overbought/oversold conditions
- Calculates momentum indicators
- Flags stocks with declining trends

### 7. **Machine Learning Model Insights**
- Historical price correlation analysis
- Sector momentum calculations
- Technical analysis with RSI and momentum metrics

## Installation

### Prerequisites
- Python 3.8+
- Perplexity API key (for LLM integration)
- pip (Python package manager)

### Steps

1. **Clone the repository:**
```bash
git clone https://github.com/Ank576/llm-powered-apps.git
cd llm-powered-apps/ai-stock-recommendation-engine
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set environment variable:**
```bash
export PERPLEXITY_API_KEY="your_api_key_here"
```

4. **Run the application:**
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

## Usage Guide

### Step 1: Portfolio Setup
1. Enter up to 5 NSE stock tickers in the sidebar (e.g., TCS.NS, INFY.NS, WIPRO.NS)
2. Specify the percentage allocation for each stock (must sum to 100%)
3. Enter your investment amount in INR

### Step 2: Investment Profile
1. Select your investment goal (Growth, Income, Capital Preservation)
2. Choose investment time horizon (Short-term, Medium-term, Long-term)
3. Select risk profile (Conservative, Moderate, Aggressive)

### Step 3: Get Recommendations
1. Click "Get AI-Powered Recommendations"
2. View portfolio metrics and technical analysis
3. Review AI-generated buy/sell/hold suggestions
4. Analyze sector overlap and rebalancing recommendations

### Example Scenario

**Portfolio:**
- TCS.NS: 30%
- INFY.NS: 25%
- WIPRO.NS: 20%
- RELIANCE.NS: 15%
- HDFC.NS: 10%

**Amount:** ₹100,000
**Time Horizon:** Long-term
**Risk Profile:** Moderate

## Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|----------|
| **UI Framework** | Streamlit 1.38.0 | Interactive web interface |
| **LLM Integration** | Perplexity API | AI-powered insights |
| **Market Data** | yfinance 0.2.32 | Real-time NSE prices |
| **Data Processing** | pandas, numpy | Analysis and calculations |
| **HTTP Client** | requests | API communication |

## API Integration

### Perplexity API
- **Endpoint:** https://api.perplexity.ai
- **Client:** OpenAI-compatible client (openai package)
- **Model:** sonar (or latest Perplexity model)
- **Purpose:** Generate market insights and recommendations

### Market Data
- **Source:** yfinance (Yahoo Finance)
- **Market:** NSE (National Stock Exchange of India)
- **Data:** Real-time prices, volume, technical indicators

## Disclaimer & Educational Notice

⚠️ **IMPORTANT - EDUCATIONAL PURPOSE ONLY**

This application is for educational and informational purposes only and should NOT be considered as:
- Financial advice
- Investment recommendations
- A substitute for professional financial advisory services
- A guarantee of investment returns

**Risk Warnings:**
1. Stock market investments carry inherent risks including potential loss of principal
2. Past performance is not indicative of future results
3. Sector and individual stock performance can be volatile
4. Leverage and margin trading amplify both gains and losses
5. Regulatory changes can significantly impact market dynamics

**User Responsibilities:**
- Conduct your own due diligence before making investment decisions
- Consult with a qualified financial advisor
- Understand the risks associated with your investment profile
- Keep up with market news and regulatory changes

**No Liability:**
The developers and maintainers of this application are not liable for any financial losses incurred as a result of using this application.

## Data Sources & References

1. **NSE Market Data:** Yahoo Finance (yfinance)
2. **Company Information:** NSE official website, financial databases
3. **Market Analysis:** Perplexity AI with real-time web search
4. **Technical Indicators:** pandas TA library methodology

## API Keys & Environment Setup

### Getting Perplexity API Key
1. Visit [Perplexity AI Platform](https://www.perplexity.ai)
2. Sign up for API access
3. Generate API key from dashboard
4. Set environment variable: `PERPLEXITY_API_KEY`

### Environment Variables
```bash
PERPLEXITY_API_KEY=your_key_here
```

## Troubleshooting

### Issue: "API Key not found"
**Solution:** Ensure `PERPLEXITY_API_KEY` environment variable is set correctly

### Issue: "Stock ticker not found"
**Solution:** Verify ticker format (must include .NS suffix for NSE stocks)

### Issue: "Portfolio percentages don't sum to 100%"
**Solution:** Adjust allocation percentages to equal exactly 100%

### Issue: "No market data available"
**Solution:** Check internet connection and ensure stock is actively trading

## Future Enhancements

- [ ] Support for additional exchanges (BSE, International)
- [ ] Machine learning model training on historical data
- [ ] Backtesting framework for strategy validation
- [ ] Portfolio performance tracking and reporting
- [ ] Advanced options and derivatives analysis
- [ ] Real-time alerts and notifications
- [ ] Export recommendations to PDF reports

## Contributing

Contributions are welcome! Please feel free to submit pull requests or report issues.

## License

This project is open source and available under the MIT License.

## Support

For questions or support, please open an issue on GitHub or contact the development team.

---

**Developed by:** Ank576  
**Repository:** [llm-powered-apps](https://github.com/Ank576/llm-powered-apps)  
**Version:** 1.0.0  
**Last Updated:** 2024
