# 🔍 AI Research Agent

An AI-powered research assistant that searches the web in real time and generates detailed, structured reports on any topic — built with LangChain, Groq (Llama 3.3), DuckDuckGo, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.3.25-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 What It Does

Instead of asking an LLM what it already knows, this agent:

1. Takes a topic from the user
2. Performs **4 targeted web searches** using DuckDuckGo
3. Aggregates all the search results
4. Feeds them to **Llama 3.3** (via Groq) to generate a structured, 600+ word report

The result is a report grounded in **real, up-to-date web data** — not just the model's training knowledge.

---

## 🧠 Tech Stack

| Layer | Technology | Cost |
|---|---|---|
| LLM | Groq API — Llama 3.3 70B | Free tier |
| Web Search | DuckDuckGo Search | Free, no API key |
| Agent Framework | LangChain 0.3 | Open source |
| UI | Streamlit | Free |
| Language | Python 3.11 | - |

---

## 🗂️ Project Structure

```
ai-research-agent/
│
├── app.py              # Streamlit UI
├── agent.py            # LLM + search logic
├── tools.py            # DuckDuckGo search tool
├── requirements.txt    # Dependencies
├── .env                # API keys (never commit this)
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

```
User types a topic
        ↓
Streamlit calls run_research()
        ↓
4 DuckDuckGo searches run (different angles of the topic)
        ↓
All results combined into a single context
        ↓
Groq (Llama 3.3) writes a structured report from the results
        ↓
Streamlit renders the markdown report
```

The report always includes:
- **Overview** — background and context
- **Key Findings** — specific facts and data points from search results
- **Deep Dive** — detailed analysis of the most important aspects
- **Conclusion** — summary and takeaways

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11
- A free [Groq API key](https://console.groq.com)

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-research-agent.git
cd ai-research-agent

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key
```

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

```bash
# 5. Run the app
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📦 Requirements

```
langchain==0.3.25
langchain-groq==0.3.2
langchain-community==0.3.23
langchain-core==0.3.58
duckduckgo-search
streamlit
python-dotenv
```

---

## 💡 Example Output

**Topic:** *"Impact of AI on healthcare in 2025"*

The agent searches for:
- `"Impact of AI on healthcare in 2025"`
- `"Impact of AI on healthcare in 2025 history and background"`
- `"Impact of AI on healthcare in 2025 details and specifications"`
- `"Impact of AI on healthcare in 2025 latest news and updates"`

Then produces a full structured report with real sources and data points.

---

## 🌐 Deployment

Deploy for free on [Streamlit Community Cloud](https://share.streamlit.io):

1. Push your code to GitHub (without `.env`)
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Add your `GROQ_API_KEY` under **App Settings → Secrets**
4. Deploy — you'll get a public URL instantly

---

## 🔮 Future Improvements

- [ ] Export report as PDF
- [ ] Show live search progress in the UI
- [ ] Add support for multiple LLM providers
- [ ] Allow users to choose number of searches
- [ ] Add a history of past research sessions

---

## 👤 Author

Built by **Charbel Farhat** as a portfolio project to demonstrate agentic AI development with LangChain and Groq.

- GitHub: [@charbel-farhat](https://github.com/charbel-farhat)
- LinkedIn: [Charbel Farhat](https://linkedin.com/in/charbeleliasfarhat)

---

## 📄 License

MIT License — feel free to use, modify, and distribute.
