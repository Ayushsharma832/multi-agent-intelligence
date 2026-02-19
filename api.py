from fastapi import FastAPI
from pydantic import BaseModel
from langgraph_orchestrator import build_graph
from fastapi.responses import HTMLResponse


app = FastAPI(title="Multi-Agent Strategic Intelligence API")

graph = build_graph()

class QueryRequest(BaseModel):
    query: str


@app.post("/analyze")
def analyze(request: QueryRequest):
    result = graph.invoke({"query": request.query})

    if result.get("general_response"):
        return {
            "mode": "general",
            "mode_reason": result.get("mode_reason"),
            "summary": result["general_response"]["summary"],
            "key_points": result["general_response"]["key_points"],
            "recommendation": result["general_response"]["recommendation"],
            "confidence_level": result["general_response"]["confidence_level"],
            "used_web_search": result.get("used_web_search", False)
        }


    return {
        "mode": "strategic",
        "mode_reason": result.get("mode_reason"),
        "final_decision": result["strategy"]["recommended_strategy"],
        "justification_summary": result["strategy"]["strategic_options"],
        "key_monitoring_metrics": result["strategy"]["execution_roadmap"]
    }


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r") as f:
        return f.read()
