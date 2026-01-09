import pathlib
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[2]
APP_DIR = ROOT / "fin-news"

def write_file(path: pathlib.Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")

def main():
    # app.py
    app_py = r"""
    import os
    import streamlit as st
    from openai import OpenAI

    PERPLEXITY_MODEL = "sonar-pro"

    def get_client():
        api_key = os.environ.get("PERPLEXITY_API_KEY")
        if not api_key:
            st.error("PERPLEXITY_API_KEY not set in environment / Streamlit secrets.")
            st.stop()
        return OpenAI(
            api_key=api_key,
            base_url="https://api.perplexity.ai"
        )

    def build_sector_prompt(sector: str, horizon: str, depth: str) -> str:
        return f"""
You are an AI financial research assistant for Indian markets.

Task:
1. Read the latest credible news and macro data for the **{sector}** sector.
2. Produce a concise **sector news feed + analysis** for an educational fintech app.
3. Time horizon: {horizon}.
4. Depth: {depth}.

Output JSON with the following keys ONLY:
- "sector_summary": 3-5 bullet points summarizing current conditions.
- "bullish_drivers": 3-5 bullet points.
- "bearish_risks": 3-5 bullet points.
- "key_news_items": list of objects:
    - "headline"
    - "source"
    - "impact" ("positive"/"negative"/"neutral")
    - "commentary" (1-2 lines).
- "macro_view": 2-3 lines on macro / policy context affecting this sector.
- "educational_disclaimer": 1-2 line disclaimer that this is NOT investment advice.

Constraints:
- Focus on Indian context (NSE/BSE, RBI/SEBI, Indian macro) where relevant.
- No stock-specific recommendations; stay at sector level.
- Keep all numbers approximate, avoid guaranteed forecasts.
- Return **valid JSON** only, no markdown or backticks.
"""

    def call_llm(client: OpenAI, prompt: str) -> dict:
        response = client.chat.completions.create(
            model=PERPLEXITY_MODEL,
            temperature=0.3,
            max_tokens=800,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a regulated-markets aware research assistant. "
                        "You provide educational, sector-level analysis only, "
                        "with no personalized investment advice."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        )
        import json
        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"raw_response": content}

    def render_news_output(data: dict):
        if "raw_response" in data:
            st.subheader("AI Response (raw)")
            st.write(data["raw_response"])
            return

        st.subheader("Sector summary")
        for item in data.get("sector_summary", []):
            st.markdown(f"- {item}")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Bullish drivers")
            for item in data.get("bullish_drivers", []):
                st.markdown(f"- {item}")
        with col2:
            st.subheader("Bearish risks")
            for item in data.get("bearish_risks", []):
                st.markdown(f"- {item}")

        st.subheader("Key news items")
        for n in data.get("key_news_items", []):
            st.markdown(
                f"**{n.get('headline', '')}**  \\n"
                f"Source: {n.get('source', 'N/A')}  \\n"
                f"Impact: {n.get('impact', 'neutral').capitalize()}  \\n"
                f"{n.get('commentary', '')}"
            )
            st.markdown("---")

        st.subheader("Macro view")
        st.write(data.get("macro_view", ""))

        st.caption(data.get("educational_disclaimer", ""))

    def main():
        st.set_page_config(
            page_title="LLM-Powered Fin-News",
            page_icon="📰",
            layout="wide",
        )

        st.title("📰 LLM-Powered Fin-News")
        st.caption(
            "Educational sector-level news & analysis for Indian markets. "
            "Not investment advice."
        )

        with st.sidebar:
            st.header("Controls")

            sector = st.selectbox(
                "Select sector",
                [
                    "Banking & Financials",
                    "Information Technology",
                    "Pharmaceuticals & Healthcare",
                    "FMCG",
                    "Automobile & Auto Ancillaries",
                    "Energy & Oil & Gas",
                    "Utilities",
                    "Real Estate",
                    "Metals & Mining",
                    "Telecom",
                    "Infrastructure",
                    "Consumer Discretionary",
                ],
            )

            horizon = st.selectbox(
                "Time horizon",
                ["Last 1 week", "Last 1 month", "Last 3 months"],
            )

            depth = st.select_slider(
                "Analysis depth",
                options=["Brief", "Standard", "In-depth"],
                value="Standard",
            )

            run_btn = st.button("Generate fin-news feed", type="primary")

        if run_btn:
            client = get_client()
            prompt = build_sector_prompt(sector, horizon, depth)

            with st.spinner(f"Fetching LLM-driven news & analysis for {sector}..."):
                data = call_llm(client, prompt)

            render_news_output(data)

    if __name__ == "__main__":
        main()
    """

    req_txt = """
    streamlit==1.38.0
    openai==1.12.0
    httpx==0.27.0
    python-dotenv>=1.0.0
    pydantic>=2.0.0
    """

    readme_md = """
    # 📰 LLM-Powered Fin-News

    **AI-powered financial sector news stream and analysis for Indian markets (NSE/BSE)**

    - 🔍 Sector selector (Banking, IT, Pharma, FMCG, Auto, Energy, etc.)
    - 📰 LLM-curated news feed with headlines, sources, and impact tags
    - 📊 Bullish / bearish drivers and macro context
    - 🛡️ Educational-only, sector-level insights (no stock tips)
    - 🤖 Powered by Perplexity `sonar-pro` via OpenAI-compatible SDK

    ## How it works

    1. User selects a **sector**, **time horizon**, and **analysis depth**.
    2. App calls Perplexity LLM with a structured JSON prompt.
    3. Response is parsed and rendered as:
       - Sector summary
       - Bullish drivers & bearish risks
       - Key news items with brief commentary
       - Macro / policy view

    ## Run locally

    ```bash
    cd fin-news
    pip install -r requirements.txt
    streamlit run app.py
    ```

    ## Compliance

    - **Purpose:** Educational sector analysis tool for learning.
    - **No personalized advice:** Does not provide stock-specific recommendations.
    - **Regulations:** Built in spirit of SEBI/RBI guidelines, but always verify with official sources.
    """

    write_file(APP_DIR / "app.py", app_py)
    write_file(APP_DIR / "requirements.txt", req_txt)
    write_file(APP_DIR / "README.md", readme_md)

    # Also append to root README if not present
    root_readme = ROOT / "README.md"
    block = textwrap.dedent("""
    ### 14. 📰 [Fin-News](./fin-news)

    **LLM-powered financial sector news stream and analysis**

    - 🔍 Sector-wise news & sentiment for Indian markets
    - 📰 Curated headlines with impact classification
    - 📊 Bullish/bearish driver breakdown and macro view
    - 🤖 JSON-structured output for easy extension

    **Compliance:** Educational tool for sector understanding – Not investment advice
    """)

    if root_readme.exists():
        content = root_readme.read_text(encoding="utf-8")
        if "Fin-News" not in content:
            root_readme.write_text(content.rstrip() + "\n\n" + block, encoding="utf-8")

if __name__ == "__main__":
    main()
