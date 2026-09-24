# AI Health Assistance 💪

A Streamlit web app that combines a **Retrieval-Augmented Generation (RAG) pipeline** with an open-weight LLM to give users personalized health metrics, an AI-generated one-day diet plan, and a grounded nutrition Q&A chatbot.

> **Live demo:** Coming soon — deployment planned via Streamlit Community Cloud / Hugging Face Spaces.

---

## 📋 Overview

Health Assistance takes basic user inputs (age, gender, height, weight, activity level, goal, diet type, and allergies) and:

1. Calculates **BMI, BMR, TDEE, and a daily calorie target** using the Mifflin–St Jeor equation.
2. Generates a **personalized one-day diet plan** (breakfast, morning snack, lunch, evening snack, dinner — with portions, calories, and protein) by combining those metrics with facts retrieved from a nutrition knowledge base.
3. Answers **free-form health & nutrition questions** through a RAG-grounded chatbot, so answers are based on retrieved source material rather than the LLM's raw output alone.

The project was built to get hands-on practice with LLM integration, prompt engineering, and Retrieval-Augmented Generation — then customized with its own calculators, prompts, and UI on top of that foundation.

---

## ✨ Features

- 🧮 Real-time **BMI / BMR / TDEE / calorie target** calculation
- 🥗 AI-generated **one-day meal plan**, respecting diet type (veg / non-veg) and stated allergies
- 💬 **RAG-powered chatbot** for open-ended health & nutrition questions
- 📚 Answers are grounded in a **nutrition knowledge base (PDF → vector search)**, not just raw LLM guesses
- 🛡️ **Prompt-level safety guardrails** — the model is explicitly instructed not to diagnose conditions, prescribe medication, or claim to cure disease, and to defer serious concerns to a healthcare professional
- 🎛️ Simple two-tab Streamlit interface (*Diet Recommendation* / *Health Assistance*)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI / Frontend | [Streamlit](https://streamlit.io/) |
| Language | Python 3 |
| LLM | `openai/gpt-oss-120b`, served via **Hugging Face Inference Providers** and called through the OpenAI-compatible Python SDK |
| RAG Orchestration | [LangChain](https://www.langchain.com/) (`langchain-community`, `langchain-text-splitters`) |
| Vector Store | [FAISS](https://github.com/facebookresearch/faiss) (`faiss-cpu`) |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` via `langchain-huggingface` |
| PDF Parsing | `pypdf` / `PyPDFLoader` |
| Config / Secrets | `python-dotenv` |

---

## 🧠 How It Works

**Knowledge base setup (one-time, offline):**
```
data/nutrition.pdf  →  PyPDFLoader  →  RecursiveCharacterTextSplitter
                                       (chunk_size=500, overlap=50)
                                    →  HuggingFace embeddings (all-MiniLM-L6-v2)
                                    →  FAISS vector index  →  saved to vector_db/
```

**At request time:**
```
User inputs (sidebar)  →  BMI / BMR / TDEE / calorie calculators (diet.py)
                                        │
User question / diet request  →  FAISS similarity search (top-3 chunks)
                                        │
                         Prompt template (prompt.md) with
                         user metrics + retrieved context
                                        │
                 openai/gpt-oss-120b via Hugging Face router
                                        │
                          Rendered back in Streamlit
```

The BMR calculation uses the **Mifflin–St Jeor equation**:
- Male:   `BMR = 10×weight + 6.25×height − 5×age + 5`
- Female: `BMR = 10×weight + 6.25×height − 5×age − 161`

TDEE is BMR scaled by an activity multiplier (1.20–1.90 depending on activity level), and the calorie target applies a ±300–400 kcal adjustment depending on whether the goal is weight loss, gain, or maintenance.

---

## 📁 Project Structure

```
Health-Assistance/
├── data/
│   └── nutrition.pdf       # Source document for the RAG knowledge base
├── app.py                  # Streamlit UI + main application logic
├── diet.py                 # BMI / BMR / TDEE / calorie-target calculators
├── rag.py                  # RAG pipeline: load PDF → chunk → embed → build/load FAISS index
├── create_database.py      # One-time script to build vector_db/ from data/nutrition.pdf
├── llm_test.py             # Standalone script to sanity-check the LLM connection
├── prompt.md                # Documented prompt templates used for the LLM calls
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```

`vector_db/` is generated locally by `create_database.py` and is not committed to the repo.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A free [Hugging Face](https://huggingface.co/) account and access token

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/Ekanshps/Health-Assistance.git
cd Health-Assistance

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root and add your Hugging Face token (get one from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)):

```
HF_TOKEN=your_hugging_face_token_here
```

### Build the knowledge base (one-time)

```bash
python create_database.py
```

This loads `data/nutrition.pdf`, chunks it, embeds it, and saves a local FAISS index to `vector_db/`.

### Run the app

```bash
streamlit run app.py
```

---

## ⚠️ Disclaimer

This project is for **educational and general wellness purposes only**. It does not diagnose, treat, or cure any medical condition and is **not a substitute for professional medical advice**. Always consult a qualified healthcare provider for medical concerns.

---

## 🗺️ Roadmap / Future Improvements

- [ ] Deploy live demo (Streamlit Community Cloud / Hugging Face Spaces)
- [ ] Add conversational memory to the Health Assistance chatbot
- [ ] Expand the nutrition knowledge base with more sources
- [ ] Support multi-day meal plans
- [ ] Add automated tests for the calculator functions
- [ ] More granular error handling (replace broad exception catches)

---

## 👤 Author

**Ekansh Pratap Singh**
MCA Student · Full-Stack & Applied AI Developer · Lucknow, India

- 🌐 Portfolio: [epsingh.in](https://epsingh.in)
- 💻 GitHub: [@Ekanshps](https://github.com/Ekanshps)
- 💼 LinkedIn: [ekanshsinghyt](https://www.linkedin.com/in/ekanshsinghyt/)
- 📧 Email: ekanshprataps@gmail.com