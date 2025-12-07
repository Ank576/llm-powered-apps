import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from openai import OpenAI
import yfinance as yf

# ═══════════════════════════════════════════════════════════════
# CONFIGURATION & SETUP
# ═══════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="💰 Dividend Income Screener",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Perplexity API client
client = OpenAI(
    api_key=st.secrets.get("PERPLEXITY_API_KEY", ""),
    base_url="https://api.perplexity.ai"
)

# ═══════════════════════════════════════════════════════════════
# DIVIDEND STOCK DATABASE (NSE)
# ═══════════════════════════════════════════════════════════════

DIVIDEND_STOCKS = {
    "Banking & Finance": {
        "SBIN.NS": {"name": "State Bank of India", "yield": 6.2, "consecutive": 45},
        "ICICIBANK.NS": {"name": "ICICI Bank", "yield": 5.8, "consecutive": 20},
        "KOTAKBANK.NS": {"name": "Kotak Mahindra Bank", "yield": 4.5, "consecutive": 15},
        "AXISBANK.NS": {"name": "Axis Bank", "yield": 5.2, "consecutive": 12},
        "HDFC.NS": {"name": "HDFC Bank", "yield": 3.5, "consecutive": 18},
        "LT.NS": {"name": "Larsen & Toubro", "yield": 5.5, "consecutive": 60},
    },
    "FMCG (Consumer Goods)": {
        "ITC.NS": {"name": "ITC Limited", "yield": 7.8, "consecutive": 50},
        "NESTLEIND.NS": {"name": "Nestle India", "yield": 2.8, "consecutive": 40},
        "BRITANNIA.NS": {"name": "Britannia Industries", "yield": 3.2, "consecutive": 30},
        "GODREJCP.NS": {"name": "Godrej Consumer", "yield": 4.1, "consecutive": 25},
        "HINDUNILVR.NS": {"name": "HUL", "yield": 3.5, "consecutive": 60},
    },
    "Healthcare & Pharma": {
        "SUNPHARMA.NS": {"name": "Sun Pharmaceutical", "yield": 4.2, "consecutive": 15},
        "CIPLA.NS": {"name": "Cipla Limited", "yield": 5.5, "consecutive": 20},
        "LUPIN.NS": {"name": "Lupin Limited", "yield": 3.8, "consecutive": 18},
        "DOCTORCARE.NS": {"name": "Dr Reddy's Labs", "yield": 2.5, "consecutive": 22},
    },
    "Energy & Utilities": {
        "POWERGRID.NS": {"name": "Power Grid Corporation", "yield": 6.8, "consecutive": 55},
        "NTPC.NS": {"name": "NTPC Limited", "yield": 7.2, "consecutive": 35},
        "RELIANCE.NS": {"name": "Reliance Industries", "yield": 2.8, "consecutive": 25},
        "GAIL.NS": {"name": "GAIL India", "yield": 8.5, "consecutive": 40},
    },
    "Real Estate (REITs)": {
        "GODREJPROP.NS": {"name": "Godrej Properties", "yield": 3.2, "consecutive": 10},
        "PHOENIXMIL.NS": {"name": "Phoenix Mills", "yield": 4.5, "consecutive": 12},
    },
    "Diversified (Multi-sector)": {
        "TCS.NS": {"name": "Tata Consultancy Services", "yield": 3.2, "consecutive": 22},
        "INFY.NS": {"name": "Infosys", "yield": 4.8, "consecutive": 20},
        "WIPRO.NS": {"name": "Wipro Limited", "yield": 5.5, "consecutive": 18},
    }
}

# Tax slab data for India (FY 2024-25)
TAX_SLABS = {
    "Upto 2.5L": {"rate": 0, "slab": "0-250000"},
    "2.5L - 5L": {"rate": 5, "slab": "250000-500000"},
    "5L - 10L": {"rate": 20, "slab": "500000-1000000"},
    "Above 10L": {"rate": 30, "slab": "1000000+"}
}

# ═══════════════════════════════════════════════════════════════
# SIDEBAR: INPUT PARAMETERS
# ═══════════════════════════════════════════════════════════════

st.sidebar.title("📊 Screening Parameters")
st.sidebar.markdown("---")

# 1. Monthly Income Requirement
st.sidebar.subheader("💵 Monthly Income Target")
monthly_income = st.sidebar.slider(
    "Required Monthly Income (₹)",
    min_value=5000,
    max_value=200000,
    value=25000,
    step=1000,
    help="Target monthly dividend income"
)

# 2. Sector Selection
st.sidebar.subheader("🏢 Sector Preference")
sector = st.sidebar.selectbox(
    "Select Sector",
    options=list(DIVIDEND_STOCKS.keys()),
    index=0,
    help="Choose preferred dividend stock sector"
)

# 3. Dividend Yield Range
st.sidebar.subheader("📈 Dividend Yield Range")
yield_range = st.sidebar.selectbox(
    "Preferred Dividend Yield",
    options=[
        "3-5% (High Stability)",
        "5-7% (Balanced)",
        "7-10% (Higher Yield)",
        "10%+ (Speculative)"
    ],
    index=1,
    help="Choose dividend yield preference"
)

# Parse yield range
yield_map = {
    "3-5% (High Stability)": (3, 5),
    "5-7% (Balanced)": (5, 7),
    "7-10% (Higher Yield)": (7, 10),
    "10%+ (Speculative)": (10, 100)
}
yield_min, yield_max = yield_map[yield_range]

# 4. Consistency Filter
st.sidebar.subheader("✅ Dividend Consistency")
min_years = st.sidebar.slider(
    "Minimum Consecutive Years of Dividends",
    min_value=1,
    max_value=60,
    value=5,
    step=1,
    help="Filter stocks with consistent dividend history"
)

consistency_filter = st.sidebar.checkbox(
    "Apply Consistency Filter",
    value=True,
    help="Show only dividend payers with unbroken record"
)

st.sidebar.markdown("---")

# ═══════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════

@st.cache_data
def filter_dividend_stocks(sector_name, yield_min, yield_max, 
                          consistency_check, min_years):
    """Filter dividend stocks based on criteria"""
    stocks = DIVIDEND_STOCKS[sector_name]
    filtered = {}
    
    for ticker, details in stocks.items():
        # Check yield range
        if not (yield_min <= details["yield"] <= yield_max):
            continue
        
        # Check consistency
        if consistency_check and details["consecutive"] < min_years:
            continue
        
        filtered[ticker] = details
    
    return filtered

def calculate_dividend_yield_needed(monthly_income, investment_amount):
    """Calculate required dividend yield to meet income goal"""
    annual_income_needed = monthly_income * 12
    required_yield = (annual_income_needed / investment_amount) * 100 if investment_amount > 0 else 0
    return required_yield

def calculate_portfolio_composition(filtered_stocks, investment_amount, monthly_target):
    """Suggest portfolio allocation"""
    if not filtered_stocks or investment_amount == 0:
        return None
    
    stocks_list = list(filtered_stocks.keys())
    n_stocks = min(len(stocks_list), 5)  # Diversify across max 5 stocks
    
    # Equal weight allocation
    amount_per_stock = investment_amount / n_stocks
    
    portfolio = []
    total_annual_income = 0
    
    for ticker in stocks_list[:n_stocks]:
        details = filtered_stocks[ticker]
        annual_dividend = (amount_per_stock * details["yield"]) / 100
        monthly_dividend = annual_dividend / 12
        
        portfolio.append({
            "Ticker": ticker,
            "Company": details["name"],
            "Amount (₹)": f"₹{amount_per_stock:,.0f}",
            "Dividend Yield": f"{details['yield']}%",
            "Annual Dividend": f"₹{annual_dividend:,.0f}",
            "Monthly Dividend": f"₹{monthly_dividend:,.0f}",
            "Consecutive Years": details["consecutive"]
        })
        total_annual_income += annual_dividend
    
    return {
        "portfolio": pd.DataFrame(portfolio),
        "total_annual": total_annual_income,
        "total_monthly": total_annual_income / 12,
        "coverage": (total_annual_income / 12) / monthly_target * 100 if monthly_target > 0 else 0
    }

def calculate_tax_impact(annual_dividend_income, tax_slab):
    """Calculate tax implications"""
    slab_info = TAX_SLABS[tax_slab]
    tax_amount = (annual_dividend_income * slab_info["rate"]) / 100
    net_income = annual_dividend_income - tax_amount
    
    return {
        "gross_annual": annual_dividend_income,
        "tax_rate": slab_info["rate"],
        "tax_amount": tax_amount,
        "net_annual": net_income,
        "net_monthly": net_income / 12
    }

def generate_ai_recommendations(filtered_stocks, portfolio_data, monthly_target, 
                              investment_amount, sector_choice):
    """Generate LLM-powered recommendations using Perplexity"""
    try:
        # Format stock data for prompt
        stocks_summary = "\n".join([
            f"- {ticker}: {details['name']} ({details['yield']}% yield, {details['consecutive']} yrs)"
            for ticker, details in list(filtered_stocks.items())[:5]
        ])
        
        prompt = f"""
        Based on the following dividend stock screening parameters, provide personalized investment recommendations:
        
        SCREENING PARAMETERS:
        - Monthly Income Target: ₹{monthly_target:,}
        - Annual Income Needed: ₹{monthly_target * 12:,}
        - Investment Amount: ₹{investment_amount:,}
        - Sector: {sector_choice}
        - Dividend Yield Range: {yield_min}-{yield_max}%
        - Consistency Filter: {min_years}+ years
        
        AVAILABLE STOCKS:
        {stocks_summary}
        
        PORTFOLIO COMPOSITION:
        Expected Monthly Income: ₹{portfolio_data['total_monthly']:,.0f}
        Income Coverage: {portfolio_data['coverage']:.1f}%
        Annual Income: ₹{portfolio_data['total_annual']:,.0f}
        
        ANALYSIS NEEDED:
        1. Stock Selection Rationale: Why these specific stocks meet the criteria
        2. Diversification Assessment: Risk profile and sector concentration
        3. Income Consistency: Analysis of dividend payment history
        4. Tax Efficiency: Impact of dividend tax on net returns
        5. Risk Factors: Key risks and mitigation strategies
        6. Portfolio Rebalancing: Suggested allocation adjustments
        7. Alternative Strategies: Other dividend stocks or investment vehicles to consider
        
        Provide actionable insights and recommendations for optimizing dividend income.
        Include RBI/SEBI compliance notes and disclaimers about investment risks.
        """
        
        response = client.messages.create(
            model="sonar",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        st.warning(f"⚠️ LLM Analysis Unavailable: {str(e)}")
        return "LLM-based analysis temporarily unavailable. Proceed with manual analysis."

# ═══════════════════════════════════════════════════════════════
# MAIN APPLICATION UI
# ═══════════════════════════════════════════════════════════════

st.title("💰 Dividend Income Screener")
st.markdown("""
**AI-Powered Dividend Stock Analysis & Portfolio Composition Tool**
- Searchable dividend stock database (NSE)
- Income goal-based screening
- Tax implications calculator
- LLM-powered recommendations
""")

st.markdown("---")

# Step 1: Filter Stocks
filtered_stocks = filter_dividend_stocks(
    sector,
    yield_min,
    yield_max,
    consistency_filter,
    min_years
)

# Display filtered stocks
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📊
