import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI
import os

st.set_page_config(page_title="💰 Dividend Income Screener", page_icon="💰", layout="wide")

client = OpenAI(api_key=os.getenv("PERPLEXITY_API_KEY", ""), base_url="https://api.perplexity.ai")

DIVIDEND_STOCKS = {
    "Banking & Finance": {
        "SBIN.NS": {"name": "State Bank of India", "yield": 6.2, "consecutive": 45},
        "ICICIBANK.NS": {"name": "ICICI Bank", "yield": 5.8, "consecutive": 20},
        "KOTAKBANK.NS": {"name": "Kotak Mahindra Bank", "yield": 4.5, "consecutive": 15},
        "AXISBANK.NS": {"name": "Axis Bank", "yield": 5.2, "consecutive": 12},
        "HDFC.NS": {"name": "HDFC Bank", "yield": 3.5, "consecutive": 18},
    },
    "FMCG (Consumer Goods)": {
        "ITC.NS": {"name": "ITC Limited", "yield": 7.8, "consecutive": 50},
        "NESTLEIND.NS": {"name": "Nestle India", "yield": 2.8, "consecutive": 40},
        "BRITANNIA.NS": {"name": "Britannia Industries", "yield": 3.2, "consecutive": 30},
        "HINDUNILVR.NS": {"name": "HUL", "yield": 3.5, "consecutive": 60},
    },
    "Energy & Utilities": {
        "POWERGRID.NS": {"name": "Power Grid Corporation", "yield": 6.8, "consecutive": 55},
        "NTPC.NS": {"name": "NTPC Limited", "yield": 7.2, "consecutive": 35},
        "GAIL.NS": {"name": "GAIL India", "yield": 8.5, "consecutive": 40},
    },
    "Healthcare & Pharma": {
        "SUNPHARMA.NS": {"name": "Sun Pharmaceutical", "yield": 4.2, "consecutive": 15},
        "CIPLA.NS": {"name": "Cipla Limited", "yield": 5.5, "consecutive": 20},
    },
    "Diversified": {
        "TCS.NS": {"name": "Tata Consultancy Services", "yield": 3.2, "consecutive": 22},
        "INFY.NS": {"name": "Infosys", "yield": 4.8, "consecutive": 20},
    }
}

TAX_SLABS = {"Upto 2.5L": 0, "2.5L - 5L": 5, "5L - 10L": 20, "Above 10L": 30}

st.title("💰 Dividend Income Screener")
st.markdown("**AI-Powered Income Screening & Portfolio Composition Tool**")

st.sidebar.header("📊 Screening Parameters")
monthly_income = st.sidebar.slider("Monthly Income Target (₹)", 5000, 200000, 25000, 1000)
sector = st.sidebar.selectbox("Select Sector", list(DIVIDEND_STOCKS.keys()))
yield_range = st.sidebar.selectbox("Dividend Yield Range", ["3-5% (High Stability)", "5-7% (Balanced)", "7-10% (Higher Yield)", "10%+ (Speculative)"])
yield_map = {"3-5% (High Stability)": (3, 5), "5-7% (Balanced)": (5, 7), "7-10% (Higher Yield)": (7, 10), "10%+ (Speculative)": (10, 100)}
yield_min, yield_max = yield_map[yield_range]
min_years = st.sidebar.slider("Min Consecutive Dividend Years", 1, 60, 5)
consistency_filter = st.sidebar.checkbox("Apply Consistency Filter", True)
investment_amount = st.sidebar.number_input("Investment Amount (₹)", 50000, 10000000, 500000, 50000)
tax_slab = st.sidebar.selectbox("Tax Slab", list(TAX_SLABS.keys()))

filtered_stocks = {}
for ticker, details in DIVIDEND_STOCKS[sector].items():
    if yield_min <= details["yield"] <= yield_max:
        if not consistency_filter or details["consecutive"] >= min_years:
            filtered_stocks[ticker] = details

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📊 Stocks Found", len(filtered_stocks))
with col2:
    required_yield = (monthly_income * 12 / investment_amount * 100) if investment_amount > 0 else 0
    st.metric("📈 Yield Needed", f"{required_yield:.2f}%")
with col3:
    st.metric("💵 Investment Amount", f"₹{investment_amount:,}")

st.markdown("---")

if filtered_stocks:
    st.subheader("📋 Suggested Portfolio Composition")
    portfolio_data = []
    total_annual = 0
    n_stocks = min(len(filtered_stocks), 5)
    
    for ticker, details in list(filtered_stocks.items())[:n_stocks]:
        amount_per_stock = investment_amount / n_stocks
        annual_dividend = (amount_per_stock * details["yield"]) / 100
        monthly_dividend = annual_dividend / 12
        total_annual += annual_dividend
        portfolio_data.append({"Ticker": ticker, "Company": details["name"], "Investment": f"₹{amount_per_stock:,.0f}", "Yield": f"{details['yield']}%", "Monthly Income": f"₹{monthly_dividend:,.0f}", "Consecutive Years": details["consecutive"]})
    
    df_portfolio = pd.DataFrame(portfolio_data)
    st.dataframe(df_portfolio, use_container_width=True)
    
    total_monthly = total_annual / 12
    coverage = (total_monthly / monthly_income * 100) if monthly_income > 0 else 0
    
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📅 Annual Income", f"₹{total_annual:,.0f}")
    with col2:
        st.metric("📊 Monthly Income", f"₹{total_monthly:,.0f}")
    with col3:
        st.metric("✅ Income Coverage", f"{coverage:.1f}%")
    with col4:
        st.metric("🎯 Target Met", "✓" if coverage >= 100 else "✗")
    
    st.markdown("---")
    st.subheader("💰 Tax Impact Analysis")
    tax_rate = TAX_SLABS[tax_slab]
    tax_amount = (total_annual * tax_rate) / 100
    net_income = total_annual - tax_amount
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"Gross Annual Income: ₹{total_annual:,.0f}")
    with col2:
        st.warning(f"Tax ({tax_rate}%): ₹{tax_amount:,.0f}")
    with col3:
        st.success(f"Net Annual Income: ₹{net_income:,.0f}")
    
    st.markdown("---")
    st.subheader("🤖 AI-Powered Recommendations")
    
    if st.button("Generate AI Insights", type="primary"):
        with st.spinner("Analyzing portfolio with AI..."):
            try:
                prompt = f"""Based on dividend stock screening:
CRITERIA: Monthly Target: ₹{monthly_income:,}, Investment: ₹{investment_amount:,}, Sector: {sector}, Yield: {yield_min}-{yield_max}%, Min Years: {min_years}
STOCKS: {', '.join([f"{t}: {d['name']} ({d['yield']}%)" for t, d in list(filtered_stocks.items())[:5]])}
METRICS: Annual Income: ₹{total_annual:,.0f}, Coverage: {coverage:.1f}%, After-Tax: ₹{net_income:,.0f}
Provide: 1. Stock rationale 2. Diversification 3. Tax strategies 4. Rebalancing 5. Risk factors 6. Alternatives. Include RBI/SEBI compliance."""
                response = client.messages.create(model="sonar", messages=[{"role": "user", "content": prompt}], max_tokens=1200)
                st.success("AI Analysis Generated")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"LLM Analysis Error: {str(e)}")
                st.info("Fallback: Use manual analysis from portfolio metrics.")
else:
    st.warning("⚠️ No stocks match your criteria. Try adjusting parameters.")

st.markdown("---")
st.markdown("""### 📋 Important Disclaimers
- **Educational Purpose**: This tool is for learning only, not investment advice
- **Tax Implications**: Consult a tax advisor for accurate tax calculations
- **Risk Disclosure**: Dividend stocks carry market risk; dividends are not guaranteed
- **Market Volatility**: Stock prices fluctuate; past yields don't guarantee future returns
- **RBI/SEBI Compliance**: Follow all regulatory requirements for investments
""")
