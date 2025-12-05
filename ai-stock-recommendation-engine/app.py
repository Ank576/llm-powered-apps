import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from openai import OpenAI
import json
import warnings
warnings.filterwarnings('ignore')

# Initialize Perplexity API client (OpenAI-compatible)
client = OpenAI(
    api_key=st.secrets.get("PERPLEXITY_API_KEY", ""),
    base_url="https://api.perplexity.ai"
)

# Streamlit page configuration
st.set_page_config(
    page_title="AI Stock Recommendation Engine",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .recommendation-buy { color: green; font-weight: bold; }
    .recommendation-sell { color: red; font-weight: bold; }
    .recommendation-hold { color: orange; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI-Powered Stock Recommendation Engine")
st.markdown("**Personalized buy/sell/hold recommendations with portfolio optimization**")

# Sidebar for user inputs
st.sidebar.header("📈 Portfolio Configuration")
st.sidebar.markdown("Enter your 5 stock holdings with allocation percentages")

# Initialize session state for stock inputs
if 'stocks' not in st.session_state:
    st.session_state.stocks = [{'ticker': '', 'percentage': 0.0} for _ in range(5)]

total_percentage = 0
stocks_list = []

cols_header = st.sidebar.columns([2, 1])
with cols_header[0]:
    st.sidebar.markdown("**Ticker**")
with cols_header[1]:
    st.sidebar.markdown("**%**")

# Stock input form
for i in range(5):
    col1, col2 = st.sidebar.columns([2, 1])
    with col1:
        ticker = st.text_input(
            f"Stock {i+1}",
            value=st.session_state.stocks[i]['ticker'],
            placeholder="e.g., INFY",
            key=f"ticker_{i}",
            label_visibility="collapsed"
        ).upper()
    with col2:
        percentage = st.number_input(
            f"% {i+1}",
            value=st.session_state.stocks[i]['percentage'],
            min_value=0.0,
            max_value=100.0,
            step=5.0,
            key=f"pct_{i}",
            label_visibility="collapsed"
        )
    
    if ticker:
        stocks_list.append(ticker)
        st.session_state.stocks[i] = {'ticker': ticker, 'percentage': percentage}
        total_percentage += percentage

# Input validation
st.sidebar.markdown("---")
if total_percentage > 0:
    if abs(total_percentage - 100.0) <= 0.1:
        st.sidebar.success(f"✅ Total: {total_percentage:.1f}%")
    else:
        st.sidebar.warning(f"⚠️ Total: {total_percentage:.1f}% (Should be 100%)")
else:
    st.sidebar.info("Enter stocks to get started")

# Goal input
user_goal = st.sidebar.selectbox(
    "📋 Investment Goal",
    ["Capital Growth", "Income Generation", "Risk Management", "Rebalancing"]
)

investment_amount = st.sidebar.number_input(
    "💰 Portfolio Value (₹)",
    value=500000,
    step=100000
)

time_horizon = st.sidebar.selectbox(
    "⏱️ Time Horizon",
    ["Short-term (< 1 year)", "Medium-term (1-3 years)", "Long-term (> 3 years)"]
)

risk_profile = st.sidebar.selectbox(
    "🎯 Risk Profile",
    ["Conservative", "Moderate", "Aggressive"]
)

# Analysis button
if st.sidebar.button("🔍 Analyze Portfolio", use_container_width=True):
    if not stocks_list:
        st.error("❌ Please enter at least one stock ticker")
    elif abs(total_percentage - 100.0) > 0.1:
        st.error("❌ Portfolio percentages must sum to 100%")
    else:
        with st.spinner("🔄 Fetching market data & analyzing portfolio..."):
            try:
                # Fetch stock data
                stock_data = {}
                for ticker in stocks_list:
                    try:
                        data = yf.Ticker(f"{ticker}.NS")
                        hist = data.history(period="1y")
                        info = data.info
                        
                        stock_data[ticker] = {
                            'current_price': hist['Close'].iloc[-1],
                            'year_high': hist['Close'].max(),
                            'year_low': hist['Close'].min(),
                            'rsi': calculate_rsi(hist['Close']),
                            'momentum': calculate_momentum(hist['Close']),
                            'sector': info.get('sector', 'Unknown')
                        }
                    except:
                        stock_data[ticker] = None
                
                # Display current portfolio
                st.header("📊 Current Portfolio Snapshot")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total Value", f"₹{investment_amount:,.0f}")
                col2.metric("Number of Holdings", len(stocks_list))
                col3.metric("Diversification Score", f"{min(100, len(stocks_list) * 15):.0f}%")
                col4.metric("Portfolio Risk", risk_profile)
                
                # Detailed holdings table
                st.subheader("💼 Holdings Breakdown")
                holdings_data = []
                for i, ticker in enumerate(stocks_list):
                    allocation = st.session_state.stocks[i]['percentage']
                    value = (investment_amount * allocation) / 100
                    if stock_data[ticker]:
                        holdings_data.append({
                            "Ticker": ticker,
                            "Allocation %": f"{allocation:.1f}%",
                            "Value": f"₹{value:,.0f}",
                            "Current Price": f"₹{stock_data[ticker]['current_price']:.2f}",
                            "RSI": f"{stock_data[ticker]['rsi']:.1f}",
                            "Sector": stock_data[ticker]['sector']
                        })
                
                df_holdings = pd.DataFrame(holdings_data)
                st.dataframe(df_holdings, use_container_width=True)
                
                st.success("✅ Analysis complete!")
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("Please check ticker symbols and ensure market data is available")

# Footer with disclaimer
st.markdown("---")
st.markdown("""
### ⚠️ Disclaimer
**Educational Purpose Only:** This tool is for educational and informational purposes only. It is NOT financial advice.
- Do NOT use as sole basis for investment decisions
- Consult with qualified financial advisors
- Past performance ≠ Future results
- Stock market carries significant risk
""")

def calculate_rsi(prices, period=14):
    """Calculate Relative Strength Index"""
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1] if not rsi.empty else 50

def calculate_momentum(prices, period=20):
    """Calculate momentum"""
    return ((prices.iloc[-1] - prices.iloc[-period]) / prices.iloc[-period]) * 100
