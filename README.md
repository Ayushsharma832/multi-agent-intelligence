Adaptive Multi-Agent Intelligence System

An intent-aware AI system built using LangGraph, FastAPI, and LLMs that dynamically routes user queries into:

📊 Strategic Business Intelligence Mode

🌐 Tool-Augmented Informational Mode

💬 Structured General Advisory Mode

This project demonstrates advanced LLM orchestration, intent classification, conditional routing, and tool-augmented reasoning in a production-style architecture.

🎯 Why This Project?

This system simulates a production-grade AI decision intelligence platform.

It showcases:

Multi-agent reasoning pipelines

Intent-aware routing

Structured output enforcement

Tool integration (web search)

Transparent AI decision behavior

API + UI integration

The goal is to demonstrate architectural thinking beyond simple prompt chaining.

🏗 Architecture Overview
User Query
      │
      ▼
Intent Classifier
      │
      ├── Strategic → Research → Risk → Finance → Strategy
      │
      ├── Informational → General Agent + Web Search
      │
      └── General → Structured Advisory Agent


The system automatically:

Classifies query intent

Routes to appropriate reasoning pipeline

Uses web search when required

Returns structured, explainable output

🚀 Features

Multi-agent orchestration using LangGraph

Intent classification layer (Strategic / Informational / General)

Conditional graph routing

Tool-augmented web search (Tavily)

Structured JSON output enforcement

Risk & strategy analysis pipeline

FastAPI backend

Minimal interactive web UI

Transparent tool usage reporting

🛠 Tech Stack

Python

LangGraph

FastAPI

Groq (LLaMA 3.1)

Tavily Web Search API

HTML / CSS / JavaScript

📦 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/multi-agent-intelligence.git
cd multi-agent-intelligence


Create virtual environment:

python -m venv venv


Activate environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

🔐 Environment Setup

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key


⚠ Do NOT commit .env to GitHub.

▶ Running the Application

Start the FastAPI server:

uvicorn api:app --reload


Open in browser:

http://127.0.0.1:8000/

📌 Example Queries
📊 Strategic Mode

Should Tesla expand into India EV market?

Is entering the EV charging infrastructure market viable?

🌐 Informational Mode

What is India GDP 2025?

Latest AI market trends in 2026?

💬 General Mode

Is having no job a good idea in 2026?

Should I wake up early?

🧩 Example Output Capabilities

Mode explanation (why system chose a specific reasoning path)

Structured response formatting

Tool usage transparency (web search indicator)

Risk scoring (Strategic mode)

Execution roadmap generation

🔮 Planned Enhancements

Risk-based conditional mitigation agent

Conversation memory layer

Execution trace visualization

Advanced logging & observability

Cloud deployment (Render / Railway)

Performance monitoring dashboard

📁 Project Structure
multi-agent-intelligence/
│
├── agents/
│   ├── research_agent.py
│   ├── risk_agent.py
│   ├── finance_agent.py
│   ├── strategy_agent.py
│   ├── domain_validator_agent.py
│   └── general_agent.py
│
├── templates/
│   └── index.html
│
├── langgraph_orchestrator.py
├── api.py
├── requirements.txt
├── README.md
└── .gitignore

👤 Author

Ayush Sharma