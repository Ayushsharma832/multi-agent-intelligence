# Adaptive Multi-Agent Intelligence System

An intent-aware multi-agent AI platform built with LangGraph, FastAPI, Groq Llama 3.1, and Tavily Search.

The system dynamically classifies user queries and routes them through specialized reasoning workflows. Strategic business questions are processed through a multi-agent pipeline consisting of Research, Risk, Finance, and Strategy agents, while informational and general queries are handled through a structured general reasoning workflow with optional real-time web search.

---

## Features

- Intent-aware query classification
- LangGraph-based workflow orchestration
- Multi-agent strategic reasoning pipeline
- Dynamic routing based on query intent
- Tool-augmented reasoning using Tavily Search
- Structured JSON output enforcement
- FastAPI REST API
- Explainable decision flow
- Transparent web-search reporting
- Interactive web interface

---

## Architecture

### Intent Classification Layer

The system first classifies incoming queries into one of three categories:

- Strategic
- Informational
- General

Example:

```json
{
  "intent": "strategic",
  "reason": "Business expansion decision detected"
}
```

---

### Routing Logic

```text
User Query
      |
      V
Intent Classifier
      |
      +----------------------+
      |                      |
      V                      V
 Strategic             Informational / General
      |                      |
      V                      V
Research Agent         General Agent
      |                      |
      V                      |
Risk Agent                  Tavily Search (optional)
      |
      V
Finance Agent
      |
      V
Strategy Agent
      |
      V
Final Response
```

---

## Strategic Intelligence Workflow

### Research Agent

Responsibilities:

- Market trends
- Competitor analysis
- Regulatory environment
- Recent developments

Uses:

- Tavily Search API

Output:

```json
{
  "market_trends": "",
  "competitors": "",
  "regulatory_environment": "",
  "recent_news": ""
}
```

---

### Risk Agent

Analyzes strategic risks:

```json
{
  "political_risk": "",
  "regulatory_risk": "",
  "competitive_risk": "",
  "economic_risk": "",
  "overall_risk_score": ""
}
```

---

### Finance Agent

Evaluates:

- Market opportunity
- Investment requirements
- Revenue potential
- Cost considerations
- ROI outlook

Output:

```json
{
  "market_opportunity": "",
  "investment_required": "",
  "revenue_potential": "",
  "cost_considerations": "",
  "roi_outlook": ""
}
```

---

### Strategy Agent

Consumes outputs from:

- Research Agent
- Risk Agent
- Finance Agent

Generates:

```json
{
  "strategic_options": "",
  "recommended_strategy": "",
  "execution_roadmap": "",
  "confidence_level": ""
}
```

---

## Informational & General Query Workflow

For non-strategic queries:

1. Determine whether real-time information is required
2. Trigger Tavily Search if needed
3. Inject search results into prompt context
4. Generate structured response

Output schema:

```json
{
  "summary": "",
  "key_points": [],
  "recommendation": [],
  "confidence_level": ""
}
```

Additional transparency field:

```json
{
  "used_web_search": true
}
```

---

## Technology Stack

### AI & Orchestration

- LangGraph
- Groq API
- Llama 3.1 8B Instant

### Search

- Tavily Search API

### Backend

- FastAPI
- Pydantic

### Frontend

- HTML Templates

### Utilities

- Python
- dotenv

---

## Project Structure

```text
multi-agent-intelligence/
│
├── agents/
│   ├── domain_validator_agent.py
│   ├── research_agent.py
│   ├── risk_agent.py
│   ├── finance_agent.py
│   ├── strategy_agent.py
│   ├── general_agent.py
│   └── synthesizer_agent.py
│
├── tools/
│   └── search_tool.py
│
├── templates/
│   └── index.html
│
├── api.py
├── langgraph_orchestrator.py
├── orchestrator.py
├── main.py
├── requirements.txt
└── README.md
```

---

## API Endpoint

### Analyze Query

```http
POST /analyze
```

Request:

```json
{
  "query": "Should Tesla expand aggressively into India in 2026?"
}
```

Response:

```json
{
  "mode": "strategic",
  "mode_reason": "Business expansion decision detected",
  "results": {}
}
```

---

## Running Locally

### Clone Repository

```bash
git clone https://github.com/Ayushsharma832/multi-agent-intelligence.git
cd multi-agent-intelligence
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

### Start FastAPI Server

```bash
uvicorn api:app --reload
```

Server:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

## Future Improvements

- Conversation memory
- Redis-based state persistence
- Agent confidence scoring
- Parallel agent execution
- Agent evaluation framework
- Human feedback loop
- Response caching
- Observability dashboards
- Docker deployment
- Authentication & rate limiting

---

## Key Design Principles

- Separation of concerns
- Explainable AI workflows
- Structured reasoning
- Tool-augmented intelligence
- Modular agent architecture
- Conditional workflow routing
- Schema-enforced outputs
