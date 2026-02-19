# 🧠 Adaptive Multi-Agent Intelligence System

An intent-aware AI system built using **LangGraph**, **FastAPI**, and **LLMs** that dynamically routes user queries into:

- 📊 Strategic Business Intelligence Mode
- 🌐 Tool-Augmented Informational Mode
- 💬 Structured General Advisory Mode

---

## 🚀 Features

- Multi-agent orchestration using LangGraph
- Intent classification layer
- Conditional routing logic
- Tool-augmented web search (Tavily)
- Structured JSON output enforcement
- Risk & strategy analysis pipeline
- FastAPI backend with interactive UI
- Transparent tool usage reporting

---

## 🏗 Architecture Overview

User Query  
→ Intent Classifier  
→ Conditional Routing  

If Strategic:
Research → Risk → Finance → Strategy  

If Informational:
General Agent + Web Search  

If General:
Structured Advisory Mode  

---

## 🛠 Tech Stack

- Python
- LangGraph
- FastAPI
- Groq LLM (LLaMA 3.1)
- Tavily Web Search
- HTML/CSS Frontend

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-intelligence.git
cd multi-agent-intelligence
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
