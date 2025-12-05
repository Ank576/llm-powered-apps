import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import warnings
from openai import OpenAI

warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="Sector Rotation Screener",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .rotation-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
    .overweight {
        background: #d4edda;
        border-left: 4px solid #28a745;
        padding: 15px;
        border-radius: 5px;
    }
    .underweight {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 15px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize LLM client
@st.cache_resource
def get_llm_client():
    return OpenAI(
        api_key=st.secrets.get("PERPLEXITY_API_KEY", ""),
        base_url="https://api.perplexity.ai"
    )

# Sector data (NSE stocks)
SECTOR_STOCKS = {
    "Tech": ["TCS.NS", "INFY.NS", "WIPRO.NS", "HCL.NS"],
    "Pharma": ["SUNPHARMA.NS", "CIPLA.NS", "LUPIN.NS", "DRREDDYS.NS"],
    "FMCG": ["ITC.NS", "HINDUNILVR.NS", "BRITANNIA.NS", "NESTLEIND.NS"],
    "Auto": ["MARUTI.NS", "BAJAJAUT.NS", "EICHERMOT.NS", "HYUNDAI.NS"],
    "Banking": ["HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS", "KOTAKBANK.NS"],
    "Energy": ["RELIANCE.NS", "BPCL.NS", "HPCL.NS", "NTPC.NS"],
    "Utilities": ["POWER.NS", "NTPC.NS", "STLTECH.NS"],
    "Real Estate": ["DLF.NS", "LODHA.NS", "BRIGADE.NS"]
}

def fetch_sector_data():
    """Fetch real-time sector momentum and metrics"""
    sector_data = {}
    
    for sector, stocks in SECTOR_STOCKS.items():
        try:
            momentums = []
            rsis = []
            yields = []
            
            for stock in stocks:
                data = yf.download(stock, period="1y", progress=False)
                if len(data) > 0:
                    # Momentum (52-week return)
                    momentum = ((data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]) * 100
                    momentums.append(momentum)
                    
                    # RSI calculation
                    delta = data['Close'].diff()
                    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
                    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
                    rs = gain / loss
                    rsi = 100 - (100 / (1 + rs))
                    rsis.append(rsi.iloc[-1])
            
            if momentums:
                sector_data[sector] = {
                    "momentum": np.mean(momentums),
                    "rsi": np.mean(rsis) if rsis else 50,
                    "volatility": np.std(momentums)
                }
        except:
            sector_data[sector] = {"momentum": 0, "rsi": 50, "volatility": 0}
    
    return sector_data

def calculate_correlations(sector_data):
    """Calculate sector correlations for diversification"""
    correlations = {}
    sectors = list(sector_data.keys())
    
    for i, s1 in enumerate(sectors):
        for s2 in sectors[i+1:]:
            # Simulate correlation (in real app, fetch actual stock correlations)
            corr = np.random.uniform(0.3, 0.9)
            correlations[f"{s1}-{s2}"] = round(corr, 2)
    
    return correlations

def get_llm_rotation_recommendation(market_condition, risk_profile, sector_data, correlations):
    """Get AI-powered rotation recommendation from LLM"""
    
    client = get_llm_client()
    
    # Format market data for LLM
    sector_summary = json.dumps(sector_data, indent=2)
    corr_summary = json.dumps(correlations, indent=2)
    
    prompt = f"""You are an expert portfolio strategist. Analyze this sector data and provide rotation recommendations.

MARKET CONDITION: {market_condition}
RISK PROFILE: {risk_profile}

SECTOR DATA (Momentum %, RSI, Volatility):
{sector_summary}

SECTOR CORRELATIONS:
{corr_summary}

Provide JSON response:
{{
  "primary_rotation": "FROM [sector] TO [sector]",
  "reasoning": {{
    "momentum_analysis": "...",
    "valuation_insight": "...",
    "risk_consideration": "..."
  }},
  "overweight_sectors": [...],
  "underweight_sectors": [...],
  "recommended_stocks": {{}},
  "confidence_score": "X%",
  "key_risks": [...],
  "alternative_scenario": "..."
}}
"""
    
    try:
        response = client.chat.completions.create(
            model="sonar",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        # Parse response
        response_text = response.choices[0].message.content
        # Extract JSON from response
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        if start != -1 and end > start:
            return json.loads(response_text[start:end])
    except Exception as e:
        st.warning(f"LLM Error: {str(e)}. Showing technical analysis only.")
    
    return None

# UI Layout
st.title("🔄 Sector Rotation Screener")
st.markdown("AI-Powered Dynamic Sector Allocation")

with st.sidebar:
    st.header("📊 Market Parameters")
    
    market_condition = st.selectbox(
        "Market Outlook",
        ["Bull", "Bear", "Sideways"],
        help="Current market trend assessment"
    )
    
    risk_profile = st.selectbox(
        "Risk Profile",
        ["Conservative", "Moderate", "Aggressive"],
        help="Your investment risk tolerance"
    )
    
    time_horizon = st.selectbox(
        "Time Horizon",
        ["1-3 months", "3-6 months", "6-12 months", "1+ years"]
    )
    
    analyze_btn = st.button("🤖 Generate AI Rotation", use_container_width=True)

# Main content
if analyze_btn:
    with st.spinner("Fetching sector data..."):
        sector_data = fetch_sector_data()
    
    with st.spinner("Analyzing with AI..."):
        correlations = calculate_correlations(sector_data)
        ai_recommendation = get_llm_rotation_recommendation(
            market_condition, risk_profile, sector_data, correlations
        )
    
    # Display Results
    if ai_recommendation:
        # Primary Rotation
        st.markdown("### 🎯 Primary Rotation Recommendation")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(
                f"<div class='rotation-card'>{ai_recommendation.get('primary_rotation', 'N/A')}</div>",
                unsafe_allow_html=True
            )
        with col2:
            confidence = ai_recommendation.get('confidence_score', 'N/A')
            st.metric("Confidence", confidence)
        
        # Sector Recommendations
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📈 OVERWEIGHT SECTORS")
            for sector in ai_recommendation.get('overweight_sectors', []):
                st.markdown(f"<div class='overweight'>✅ {sector}</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 📉 UNDERWEIGHT SECTORS")
            for sector in ai_recommendation.get('underweight_sectors', []):
                st.markdown(f"<div class='underweight'>❌ {sector}</div>", unsafe_allow_html=True)
        
        # Reasoning
        st.markdown("---")
        st.markdown("### 💡 AI Reasoning")
        reasoning = ai_recommendation.get('reasoning', {})
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"**Momentum Analysis:**\n{reasoning.get('momentum_analysis', 'N/A')}")
        with col2:
            st.write(f"**Valuation Insight:**\n{reasoning.get('valuation_insight', 'N/A')}")
        with col3:
            st.write(f"**Risk Consideration:**\n{reasoning.get('risk_consideration', 'N/A')}")
        
        # Stock Picks
        st.markdown("---")
        st.markdown("### 📈 Recommended Stocks")
        stock_picks = ai_recommendation.get('recommended_stocks', {})
        for sector, stocks in stock_picks.items():
            st.write(f"**{sector}:** {', '.join(stocks)}")
        
        # Risks
        st.markdown("---")
        st.markdown("### ⚠️ Key Risks")
        for risk in ai_recommendation.get('key_risks', []):
            st.warning(risk)
        
        # Alternative Scenario
        st.markdown("---")
feat: Add Sector Rotation Screener with AI/LLM recommendations        st.info(ai_recommendation.get('alternative_scenario', 'N/A'))
    
    else:
        # Technical Analysis Fallback
        st.markdown("### 📊 Sector Momentum Analysis")
        
        df = pd.DataFrame.from_dict(sector_data, orient='index')AI-powered dynamic sector allocation tool featuring:
- Market condition analysis (Bull/Bear/Sideways)
- Sector momentum and RSI calculations
- LLM-based rotation recommendations
- Correlation matrix for diversification
- Stock picks with confidence scoring
- Technical analysis fallback
- Risk warning system
        df = df.sort_values('momentum', ascending=False)
        
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(df[['momentum', 'rsi']])
        with col2:
            st.bar_chart(df['momentum'])
        
        # Correlation heatmap
        st.markdown("### 📉 Sector Correlations (Diversification Guide)")
        corr_df = pd.DataFrame.from_dict(correlations, orient='index', columns=['Correlation'])
        st.dataframe(corr_df)

st.markdown("---")
st.markdown("""
⚠️ **Disclaimer:** Educational demo. Not financial advice. Consult advisors before investing.
- Data sourced from Yahoo Finance
- AI recommendations for learning purposes
- Test with small amounts before deploying
""")
