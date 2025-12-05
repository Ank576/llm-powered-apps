import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Value Stock Finder",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
    .undervalued-stock {
        background: #d4edda;
        border-left: 4px solid #28a745;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .fair-value-stock {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .overvalued-stock {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Helper functions
@st.cache_data
def get_stock_data(ticker, period="5y"):
    """Fetch stock data from yfinance"""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        return stock.info, hist
    except:
        return None, None

def calculate_graham_number(eps, book_value_per_share, growth_rate=15):
    """Calculate Graham Number (Intrinsic Value)"""
    if eps <= 0 or book_value_per_share <= 0:
        return None
    graham_number = np.sqrt(22.5 * eps * book_value_per_share)
    return graham_number

def calculate_valuation_metrics(info, current_price):
    """Calculate various valuation metrics"""
    metrics = {}
    
    # P/E Ratio
    metrics['pe_ratio'] = current_price / info.get('trailingEps', 1) if info.get('trailingEps') else None
    
    # P/B Ratio
    metrics['pb_ratio'] = info.get('priceToBook', None)
    
    # P/S Ratio
    market_cap = info.get('marketCap', 0)
    revenue = info.get('totalRevenue', 0)
    metrics['ps_ratio'] = (market_cap / revenue) if revenue > 0 else None
    
    # EPS
    metrics['eps'] = info.get('trailingEps', None)
    
    # ROE
    metrics['roe'] = info.get('returnOnEquity', None)
    
    # ROA
    metrics['roa'] = info.get('returnOnAssets', None)
    
    # Debt to Equity
    metrics['debt_to_equity'] = info.get('debtToEquity', None)
    
    return metrics

def get_valuation_score(metrics, current_price, graham_number=None):
    """Calculate overall valuation score (0-100)"""
    score = 50  # Base score
    
    # P/E Ratio scoring (Lower is better for value)
    if metrics['pe_ratio']:
        if metrics['pe_ratio'] < 15:
            score += 20
        elif metrics['pe_ratio'] < 20:
            score += 10
        elif metrics['pe_ratio'] > 30:
            score -= 15
    
    # P/B Ratio scoring
    if metrics['pb_ratio']:
        if metrics['pb_ratio'] < 1:
            score += 15
        elif metrics['pb_ratio'] < 1.5:
            score += 8
    
    # Graham Number comparison
    if graham_number and current_price < graham_number:
        discount = ((graham_number - current_price) / graham_number) * 100
        if discount > 20:
            score += 15
        elif discount > 10:
            score += 8
    
    # ROE scoring (Higher is better)
    if metrics['roe'] and metrics['roe'] > 0:
        if metrics['roe'] > 0.15:
            score += 10
        elif metrics['roe'] > 0.10:
            score += 5
    
    # Debt to Equity
    if metrics['debt_to_equity'] and metrics['debt_to_equity'] < 1:
        score += 5
    
    return min(max(score, 0), 100)

# Title
st.title("📈 Value Stock Finder")
st.markdown("### Discover Undervalued Stocks Using Financial Metrics")
st.markdown("""
This educational tool helps identify potentially undervalued stocks based on fundamental analysis.
It uses metrics like P/E ratio, Graham Number, ROE, and more.
""")

st.warning("⚠️ **Disclaimer**: This is an educational demo. Always conduct thorough research and consult financial advisors before investing.")

# Sidebar inputs
with st.sidebar:
    st.header("🔍 Filter Criteria")
    
    stock_ticker = st.text_input(
        "Stock Ticker (e.g., RELIANCE.NS, TCS.NS)",
        value="RELIANCE.NS",
        help="NSE stocks use .NS suffix. E.g., INFY.NS, WIPRO.NS"
    )
    
    max_pe = st.slider(
        "Maximum P/E Ratio",
        min_value=5,
        max_value=50,
        value=20,
        help="Lower P/E = potentially undervalued"
    )
    
    min_roe = st.slider(
        "Minimum ROE (%)",
        min_value=0,
        max_value=100,
        value=15,
        step=5,
        help="Return on Equity - higher is better"
    )
    
    max_debt_equity = st.slider(
        "Maximum Debt-to-Equity",
        min_value=0.0,
        max_value=2.0,
        value=1.0,
        step=0.1,
        help="Lower is safer - less financial risk"
    )
    
    analyze_btn = st.button("🔎 Analyze Stock", use_container_width=True)

# Main analysis
if analyze_btn or stock_ticker:
    with st.spinner(f"Analyzing {stock_ticker}..."):
        info, hist = get_stock_data(stock_ticker)
        
        if info is None:
            st.error(f"❌ Could not fetch data for {stock_ticker}. Please check the ticker symbol.")
        else:
            current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
            
            # Calculate metrics
            metrics = calculate_valuation_metrics(info, current_price)
            
            # Calculate Graham Number
            eps = metrics['eps']
            book_value = info.get('bookValue', None)
            graham_number = calculate_graham_number(eps, book_value) if eps and book_value else None
            
            # Get valuation score
            valuation_score = get_valuation_score(metrics, current_price, graham_number)
            
            # Display results
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Current Price", f"₹{current_price:.2f}")
            
            with col2:
                st.metric("P/E Ratio", f"{metrics['pe_ratio']:.2f}" if metrics['pe_ratio'] else "N/A")
            
            with col3:
                st.metric("ROE", f"{(metrics['roe']*100):.2f}%" if metrics['roe'] else "N/A")
            
            with col4:
                st.metric("Valuation Score", f"{valuation_score}/100")
            
            # Valuation status
            st.markdown("---")
            st.subheader("💎 Valuation Analysis")
            
            if valuation_score >= 70:
                status = "undervalued-stock"
                emoji = "✅"
                message = f"**UNDERVALUED**: Strong value signal! Stock appears undervalued."
            elif valuation_score >= 50:
                status = "fair-value-stock"
                emoji = "⚠️"
                message = f"**FAIR VALUE**: Stock is reasonably valued."
            else:
                status = "overvalued-stock"
                emoji = "❌"
                message = f"**OVERVALUED**: Stock appears expensive relative to fundamentals."
            
            st.markdown(f'<div class="{status}"> {emoji} {message} </div>', unsafe_allow_html=True)
            
            # Detailed metrics
            st.markdown("---")
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📊 Valuation Metrics")
                valuation_data = {
                    "Metric": ["P/E Ratio", "P/B Ratio", "P/S Ratio"],
                    "Value": [
                        f"{metrics['pe_ratio']:.2f}" if metrics['pe_ratio'] else "N/A",
                        f"{metrics['pb_ratio']:.2f}" if metrics['pb_ratio'] else "N/A",
                        f"{metrics['ps_ratio']:.2f}" if metrics['ps_ratio'] else "N/A"
                    ]
                }
                st.dataframe(pd.DataFrame(valuation_data), use_container_width=True)
            
            with col2:
                st.subheader("💰 Profitability & Health")
                health_data = {
                    "Metric": ["ROE", "ROA", "Debt-to-Equity"],
                    "Value": [
                        f"{(metrics['roe']*100):.2f}%" if metrics['roe'] else "N/A",
                        f"{(metrics['roa']*100):.2f}%" if metrics['roa'] else "N/A",
                        f"{metrics['debt_to_equity']:.2f}" if metrics['debt_to_equity'] else "N/A"
                    ]
                }
                st.dataframe(pd.DataFrame(health_data), use_container_width=True)
            
            # Graham Number
            if graham_number:
                st.markdown("---")
                st.subheader("🎯 Intrinsic Value (Graham Number)")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Graham Number", f"₹{graham_number:.2f}")
                with col2:
                    discount = ((graham_number - current_price) / graham_number) * 100
                    st.metric("Discount to Fair Value", f"{discount:.2f}%")
                with col3:
                    upside = ((graham_number - current_price) / current_price) * 100
                    st.metric("Upside Potential", f"{upside:.2f}%")
                
                st.info(f"📌 **Graham Number**: An intrinsic value estimate. If current price < Graham Number, stock may be undervalued.")
            
            # Key insights
            st.markdown("---")
            st.subheader("💡 Key Insights")
            
            insights = []
            
            if metrics['pe_ratio'] and metrics['pe_ratio'] < max_pe:
                insights.append(f"✅ P/E Ratio ({metrics['pe_ratio']:.2f}) is below your threshold ({max_pe})")
            elif metrics['pe_ratio']:
                insights.append(f"❌ P/E Ratio ({metrics['pe_ratio']:.2f}) exceeds threshold ({max_pe})")
            
            if metrics['roe'] and metrics['roe'] * 100 > min_roe:
                insights.append(f"✅ ROE ({metrics['roe']*100:.2f}%) exceeds your minimum ({min_roe}%)")
            elif metrics['roe']:
                insights.append(f"❌ ROE ({metrics['roe']*100:.2f}%) is below your minimum ({min_roe}%)")
            
            if metrics['debt_to_equity'] and metrics['debt_to_equity'] < max_debt_equity:
                insights.append(f"✅ Debt-to-Equity ({metrics['debt_to_equity']:.2f}) is healthy")
            elif metrics['debt_to_equity']:
                insights.append(f"⚠️ Debt-to-Equity ({metrics['debt_to_equity']:.2f}) is elevated")
            
            for insight in insights:
                st.write(insight)

# Footer
st.markdown("---")
st.markdown("""
**Disclaimer**: This tool is for educational purposes only. It provides simplified valuation metrics.
Always conduct thorough due diligence and consult with a financial advisor before making investment decisions.

**How it works**:
1. Enter a stock ticker (NSE tickers use .NS suffix)
2. Adjust filter criteria based on your investment preferences
3. Review valuation metrics and insights
4. Cross-reference with other research sources
""")
