# 🔄 Sector Rotation Screener - AI-Powered Portfolio Recommendations

**An intelligent stock screening tool that combines technical analysis with LLM-powered AI reasoning to identify optimal sector rotation opportunities in the Indian stock market.**

---

## 📄 Overview

The Sector Rotation Screener is an advanced Streamlit-based application that leverages **Perplexity LLM** to provide AI-powered sector rotation recommendations. Unlike traditional technical analysis tools, this application integrates artificial intelligence reasoning to analyze market conditions, compare sector strength, and suggest strategic sector shifts for portfolio optimization.

### Key Innovation: LLM-Integrated Analysis

This application combines:
- **Technical Analysis**: RSI, Momentum calculations
- **Statistical Analysis**: Correlation matrices, relative strength comparison
- **AI Reasoning**: Perplexity LLM for strategic insights and recommendations

The LLM analyzes market data and generates human-readable insights, including specific sector rotation recommendations ("From TECH -> To PHARMA"), reasoning behind the moves, and risk assessments.

---

## ✨ Features

### 1. Market Condition Analysis
- Select market conditions: Bull, Bear, or Sideways
- Specify risk profile: Conservative, Moderate, or Aggressive
- Real-time data fetching from NSE stocks (yfinance)

### 2. Sector Momentum Analysis
- Calculates 20-day and 50-day momentum for 8 major sectors
- Measures relative strength using RSI (Relative Strength Index)
- Provides sector-level performance metrics
- 8 Covered Sectors:
  - Technology (TCS, Infosys, Wipro, HCL Tech, Persistent, Mindtree)
  - Pharmaceuticals (Cipla, Dr. Reddy's, Lupin, Aurobindo, Divis Labs)
  - FMCG (ITC, HUL, Britannia, Nestle India, Marico, Godrej Consumer)
  - Automobiles (Maruti, Hero, Bajaj, TVS, Ashok Leyland, M&M)
  - Banking (HDFC Bank, ICICI Bank, Axis Bank, Kotak Bank, IndusInd)
  - Energy (Reliance, ONGC, Power Grid, Coal India)
  - Utilities (NTPC, DLF, Oberoi Realty, Lodha)
  - Real Estate (DLF, Prestige, Oberoi, Lodha)

### 3. Correlation Analysis
- Computes pairwise sector correlations
- Identifies diversification opportunities
- Visualizes correlation heatmap
- Recommends low-correlation portfolio combinations

### 4. AI-Powered LLM Integration
- Perplexity API Integration: Uses OpenAI-compatible client
- Intelligent Prompting: Engineered prompts to extract structured sector recommendations
- JSON Response Parsing: Parses LLM output for:
  - Recommended sectors to overweight/underweight
  - Rotation suggestions ("From -> To")
  - AI reasoning and market analysis
  - Confidence scores
  - Risk assessment metrics

### 5. Sector Rotation Recommendations
- Displays LLM-generated "FROM -> TO" rotation suggestions
- Color-coded indicators:
  - GREEN for overweight sectors
  - RED for underweight sectors
- AI reasoning explaining each recommendation
- Confidence scores for each rotation

### 6. Risk Assessment
- Correlation-based diversification warnings
- Portfolio concentration alerts
- Market volatility considerations
- Sector interdependency analysis

### 7. Fallback Mechanism
- If Perplexity API unavailable, app displays technical analysis dashboard
- Technical analysis provides RSI, momentum, and correlation insights
- Ensures reliable functionality regardless of API availability

---

## 🔗 LLM Integration Architecture

### Data Pipeline Flow

1. **INPUT STAGE**
   - Market Condition (Bull/Bear/Sideways)
   - Risk Profile (Conservative/Moderate/Aggressive)
   - Time Period (20-day, 50-day momentum)

2. **DATA FETCHING**
   - yfinance -> NSE Stock Data
   - Calculate RSI for all 8 sectors
   - Compute momentum values
   - Build correlation matrix

3. **PROMPT ENGINEERING**
   - Aggregate sector metrics
   - Construct detailed prompt
   - Include market context and risk parameters
   - Request JSON-formatted response

4. **LLM PROCESSING (Perplexity API)**
   - Send engineered prompt
   - Process with Perplexity LLM
   - Extract structured response
   - Parse JSON recommendations

5. **OUTPUT STAGE**
   - Display overweight/underweight sectors
   - Show rotation recommendations
   - Present AI reasoning
   - Visualize correlations
   - Provide risk warnings

### Prompt Engineering Example

The application crafts sophisticated prompts to get structured recommendations:

**Sample Input:**
```
Market Condition: Bull Market
Risk Profile: Aggressive
Tech Momentum (20d): +2.5%, RSI: 65
Pharma Momentum (20d): -1.2%, RSI: 35
...
Request: Suggest sector rotations and provide JSON with overweight_sectors, underweight_sectors, rotations, reasoning, confidence_score
```

**Expected LLM Response:**
```json
{
  "overweight_sectors": ["Technology", "Banking"],
  "underweight_sectors": ["Pharmaceuticals", "Utilities"],
  "rotations": [
    {"from": "Pharma", "to": "Tech", "reason": "Momentum shift towards growth"}
  ],
  "reasoning": "Bull market with strong tech momentum and weak pharma sentiment",
  "confidence_score": 0.82
}
```

---

## 💻 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- NSE Historical Stock Data (via yfinance)
- Perplexity API Key (free tier available)

### Step 1: Clone Repository
```bash
git clone https://github.com/Ank576/llm-powered-apps.git
cd llm-powered-apps/sector-rotation-screener
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Environment Variables
```bash
export PERPLEXITY_API_KEY="your-perplexity-api-key"
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📑 Usage Guide

### Quick Start

1. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

2. **Configure Parameters** (Sidebar)
   - Select Market Condition: Bull, Bear, or Sideways
   - Choose Risk Profile: Conservative, Moderate, or Aggressive
   - App will analyze NSE stock data

3. **View Analysis** (Main Dashboard)
   - Sector momentum metrics (20-day, 50-day)
   - RSI values and momentum indicators
   - AI-generated sector recommendations
   - Correlation matrix heatmap

4. **Interpret Recommendations**
   - Green indicators = Overweight (increase exposure)
   - Red indicators = Underweight (reduce exposure)
   - Read confidence score (0-1 scale)
   - Study AI reasoning for market insights

### Example Workflow

**Scenario: Bull Market, Aggressive Profile**
1. Select "Bull" market condition
2. Choose "Aggressive" risk profile
3. View recommendations
4. Expected output: Growth sectors (Tech, Pharma, Banking) overweighted
5. Defensive sectors (Utilities, Energy) underweighted
6. Example rotation: FMCG -> Technology

**Scenario: Bear Market, Conservative Profile**
1. Select "Bear" market condition
2. Choose "Conservative" risk profile
3. View recommendations
4. Expected output: Defensive sectors overweighted
5. Growth sectors underweighted
6. Example rotation: Tech -> Utilities

---

## 📚 Technical Stack

- **Frontend**: Streamlit 1.38.0 (Interactive Web UI)
- **Data Fetching**: yfinance 0.2.32 (NSE Historical Data)
- **Data Processing**: pandas 2.1.4, numpy 1.24.3
- **LLM Integration**: openai 1.3.8 (Perplexity API via OpenAI-compatible)
- **Analysis**: Technical indicators (RSI, Momentum)
- **Visualization**: Streamlit built-in charting

---

## 🎓 Educational Value

### What Users Learn

1. **Sector Rotation Strategy**
   - Understanding market cycles (Bull/Bear/Sideways)
   - Sector performance correlation
   - Risk-adjusted portfolio rotation

2. **Technical Analysis**
   - RSI interpretation (Overbought/Oversold)
   - Momentum analysis and trend identification
   - Correlation-based diversification

3. **AI in Finance**
   - LLM integration for financial analysis
   - Prompt engineering for structured outputs
   - Combining technical analysis with AI reasoning

4. **Risk Management**
   - Portfolio concentration assessment
   - Sector interdependency analysis
   - Diversification strategies

---

## 📊 Market Data & Sectors

### Data Source
- **Primary**: yfinance (Yahoo Finance API)
- **Market**: National Stock Exchange (NSE) - India
- **Stock Suffix**: .NS (e.g., TCS.NS, INFY.NS)
- **Historical Period**: 1 year (default)
- **Update Frequency**: Real-time (updated on each app run)

### Sector Coverage

**Technology Sector**
Companies: TCS, Infosys, Wipro, HCL Tech, Persistent, Mindtree
Key Metrics: Revenue growth, profit margins, digital transformation

**Pharmaceutical Sector**
Companies: Cipla, Dr. Reddy's, Lupin, Aurobindo, Divis Labs
Key Metrics: Drug pipeline, regulatory approvals, export strength

**FMCG Sector**
Companies: ITC, HUL, Britannia, Nestle India, Marico, Godrej Consumer
Key Metrics: Volume growth, pricing power, rural penetration

**Automobile Sector**
Companies: Maruti, Hero MotoCorp, Bajaj, TVS, Ashok Leyland, M&M
Key Metrics: Vehicle sales, export orders, electric vehicle transition

**Banking Sector**
Companies: HDFC Bank, ICICI Bank, Axis Bank, Kotak Bank, IndusInd
Key Metrics: NPA ratios, deposit growth, credit expansion

**Energy Sector**
Companies: Reliance Industries, ONGC, Power Grid Corporation, Coal India
Key Metrics: Oil prices, gas production, renewable energy transition

**Utilities Sector**
Companies: NTPC, DLF, Oberoi Realty, Lodha
Key Metrics: Power generation, renewable capacity, tariff rates

**Real Estate Sector**
Companies: DLF, Prestige, Oberoi Properties, Lodha Group
Key Metrics: Project launches, sales velocity, project completions

---

## ⚖️ Disclaimers & Important Notes

### CRITICAL - EDUCATIONAL PURPOSE ONLY

**This application is for educational and informational purposes only.**

1. **Not Investment Advice**
   - These recommendations are NOT financial advice
   - Do NOT use this tool as sole basis for investment decisions
   - Consult with qualified financial advisors before investing

2. **Risk Acknowledgment**
   - Stock market investments carry significant risk
   - Past performance does NOT guarantee future results
   - You may lose part or all of your investment

3. **LLM Limitations**
   - AI-generated insights can be incorrect
   - LLM may hallucinate or misinterpret data
   - Manual verification of recommendations is essential

4. **Data Accuracy**
   - yfinance data may have delays or inaccuracies
   - NSE official sources should be primary reference
   - Real-time trading uses different data feeds

5. **Regulatory Compliance (India)**
   - SEBI (Securities and Exchange Board of India) regulations apply
   - RBI (Reserve Bank of India) guidelines for financial products
   - Ensure compliance with local investment rules

6. **Market Conditions**
   - Recommendations assume normal market conditions
   - Extreme volatility may invalidate assumptions
   - Sector rotation benefits require active monitoring

---

## Troubleshooting

### Common Issues

**Issue: API Key Not Found**
```
Error: PERPLEXITY_API_KEY environment variable not set
```
Solution: Set the environment variable before running the app
```bash
export PERPLEXITY_API_KEY="your-key-here"
```

**Issue: No Data for Stock**
```
Error: Unable to fetch data for TCS.NS
```
Solution:
- Check internet connection
- Verify stock symbol with .NS suffix
- Try again (yfinance may have temporary issues)

**Issue: LLM Not Responding**
```
Falling back to technical analysis dashboard
```
Solution:
- Check Perplexity API key is valid
- Verify API rate limits not exceeded
- Technical analysis will still display

**Issue: Slow Performance**
Solution:
- First run may be slower (downloading 1 year data)
- Reduce number of stocks per sector
- Increase Streamlit cache timeout

---

## Limitations

1. **Data Limitations**
   - Only covers 8 sectors (32 major stocks)
   - 1-year historical data window
   - NSE stocks only (no international)

2. **LLM Limitations**
   - Perplexity API has rate limits
   - JSON parsing may fail with malformed responses
   - AI reasoning may be market-biased

3. **Technical Analysis Limitations**
   - RSI 14-period may not capture short-term reversals
   - Momentum calculations use simple 20/50-day periods
   - Correlation assumes historical patterns continue

4. **Market Coverage**
   - No options/futures analysis
   - No dividend-adjusted returns
   - No sector indices (only stock-based)

---

## Future Enhancements

1. **Extended Sector Coverage**
   - Add commodity sectors (Metals, Mining)
   - Include defense & aerospace
   - Expand to 50+ stocks per analysis

2. **Advanced Technical Indicators**
   - MACD, Bollinger Bands, Stochastic
   - Volume-weighted analysis
   - Options implied volatility

3. **Enhanced AI Features**
   - Multi-model LLM comparison (GPT-4, Claude)
   - Fine-tuned models for Indian market
   - Sentiment analysis from news feeds

4. **Backtesting Framework**
   - Historical performance testing
   - Monte Carlo simulations
   - Risk-adjusted return calculations

5. **Portfolio Management**
   - Track recommended rotations
   - Performance attribution analysis
   - Rebalancing suggestions

6. **Data Enhancements**
   - Real-time data feeds
   - Fundamental analysis (PE, PB ratios)
   - Insider trading alerts

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Test thoroughly
4. Submit a pull request with description

Areas for contribution:
- Adding new sectors/stocks
- Improving LLM prompts
- Enhancing visualizations
- Fixing bugs and improving documentation

---

## References & Resources

- Perplexity LLM Documentation: https://docs.perplexity.ai
- Streamlit Documentation: https://docs.streamlit.io
- yfinance GitHub: https://github.com/ranaroussi/yfinance
- NSE India: https://www.nseindia.com
- SEBI Guidelines: https://www.sebi.gov.in
- RBI Monetary Policy: https://www.rbi.org.in
- Technical Analysis: https://www.investopedia.com/terms/t/technicalanalysis.asp
- Sector Rotation: https://en.wikipedia.org/wiki/Sector_rotation

---

## License

This project is open source and available for educational use.

---

**Made with love for the Indian investing community**

*Sector Rotation Screener v1.0 - 2024*
