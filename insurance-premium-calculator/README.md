# 🛡️ IRDA-Compliant Insurance Premium Estimator

AI-powered Streamlit app that provides **indicative premium estimates** for **life, term, and health insurance** in India. The app uses an LLM to suggest product mixes, estimate premiums, and highlight **tax benefits under Section 80D and 80C**, while keeping the experience aligned with **IRDA guidelines**.

> ⚠️ **Important:** This tool is for **educational and demo purposes only**. It does **not** replace advice from IRDA-registered insurers, corporate agents, or financial advisors.

---

## ✨ Key Features

- Indicative premium estimation for:
  - Term insurance
  - Life insurance
  - Health insurance (individual / family floater)
- Profile-based recommendations using:
  - Age, gender, city type (metro / non-metro)
  - Income and dependents
  - Health conditions and lifestyle factors
  - Smoker / non-smoker status
- Tax benefit estimation:
  - Section **80D** (health insurance premium)
  - Section **80C** (life / term premiums, where applicable)
- IRDA-aligned notes:
  - Proposal form & medical underwriting
  - KYC requirements
  - Free-look period and disclosures
- JSON-structured responses from Perplexity LLM for reliable parsing

---

## 🧱 Tech Stack

| Technology | Purpose |
|-----------|---------|
| Streamlit | UI layer for user inputs and results |
| Perplexity LLM (`sonar-pro`) | Insurance reasoning, premium and product suggestion engine |
| httpx | HTTP client for Perplexity API |
| Python 3.11+ | Runtime |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Ank576/insurance-premium-calculator.git
cd insurance-premium-calculator
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Perplexity API Key

Export your Perplexity API key as an environment variable or use Streamlit secrets.

#### Option A: Environment variable

```bash
export PERPLEXITY_API_KEY="pplx-..."  # macOS / Linux
set PERPLEXITY_API_KEY="pplx-..."      # Windows
```

#### Option B: Streamlit secrets

Create a `.streamlit/secrets.toml` file:

```toml
PERPLEXITY_API_KEY = "pplx-..."
```

---

### 5. Run the App

```bash
streamlit run app.py
```

Open the URL shown in the terminal (typically `http://localhost:8501`).

---

## 🧮 How It Works

1. User enters profile details (age, income, health, lifestyle, coverage needs, family structure).
2. The app builds a **structured prompt** for the LLM with these details.
3. Perplexity's `sonar-pro` model returns a **JSON object** containing:
   - Eligibility flag
   - Recommended insurance product mix
   - Coverage, annual and monthly premium estimates
   - Tax benefit estimates under Section 80D and 80C
   - Risk summary and IRDA-related notes
4. Streamlit renders the recommendations as expandable cards, metrics, and explanatory notes.

All numbers are **indicative** and meant for planning and demonstration only.

---

## 📌 Disclaimers & Compliance

- This project is **not an insurance distributor** and does not sell or solicit any policy.
- Premiums and tax benefits shown are **approximate** and for **educational use**.
- Actual premiums depend on:
  - Insurer underwriting policies
  - Medical tests and health disclosures
  - Correct completion of proposal form
  - Applicable IRDA regulations and tax laws at the time of purchase
- Users should always verify details with:
  - IRDA-registered insurers
  - Licensed individual/corporate agents
  - Certified financial or tax advisors

---

## 🧪 Ideas for Future Enhancements

- Add insurer-specific product examples (without branding) for clearer ranges.
- Allow CSV export of results for client advisory workflows.
- Add support for senior citizen-specific plan explanations.
- Build a comparison view for different coverage scenarios (e.g., 50L vs 1Cr term).

---

## 📄 License

MIT License. See `LICENSE` if added.

---

## ⭐ Support

If this project helps showcase your AI + fintech skills, consider **starring the repo** and reusing the pattern in your `llm-powered-apps` monorepo.
