from typing import TypedDict
from langgraph.graph import StateGraph, END

# Import existing agents
from agents.research_agent import research_agent
from agents.risk_agent import risk_agent
from agents.finance_agent import finance_agent
from agents.strategy_agent import strategy_agent
from agents.synthesizer_agent import synthesizer_agent
from agents.domain_validator_agent import domain_validator_agent
from agents.general_agent import general_agent



class AgentState(TypedDict):
    query: str
    is_business_query: bool
    mode_reason: str
    general_response: str
    used_web_search: bool
    research: dict
    risk: dict
    finance: dict
    strategy: dict
    final_decision: dict

def validation_node(state: AgentState):
    result = domain_validator_agent(state["query"])

    return {
        "is_business_query": result["is_business_query"],
        "mode_reason": result["reason"]
    }


def general_node(state: AgentState):
    result = general_agent(state["query"])

    return {
        "general_response": result["response"],
        "used_web_search": result["used_web_search"]
    }



def research_node(state: AgentState):
    result = research_agent(state["query"])
    return {"research": result}


def risk_node(state: AgentState):
    result = risk_agent(state["research"])
    return {"risk": result}


def finance_node(state: AgentState):
    result = finance_agent(state["research"])
    return {"finance": result}


def strategy_node(state: AgentState):
    result = strategy_agent(
        state["research"],
        state["risk"],
        state["finance"]
    )
    return {"strategy": result}


def synthesis_node(state: AgentState):
    result = synthesizer_agent(
        state["risk"],
        state["finance"],
        state["strategy"]
    )
    return {"final_decision": result}

def build_graph():

    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("validation", validation_node)
    workflow.add_node("general", general_node)
    workflow.add_node("research", research_node)
    workflow.add_node("risk", risk_node)
    workflow.add_node("finance", finance_node)
    workflow.add_node("strategy", strategy_node)
    workflow.add_node("synthesis", synthesis_node)
    


    # Define execution flow
    workflow.set_entry_point("validation")

    def route_query(state: AgentState):
        if state["is_business_query"]:
            return "research"
        else:
            return "general"

    workflow.add_conditional_edges(
            "validation",
            route_query
        )

    workflow.add_edge("general", END)
    workflow.add_edge("research", "risk")
    workflow.add_edge("risk", "finance")
    workflow.add_edge("finance", "strategy")
    workflow.add_edge("strategy", "synthesis")
    workflow.add_edge("synthesis", END)



    return workflow.compile()

if __name__ == "__main__":
    graph = build_graph()

    result = graph.invoke({
        "query": "Should Tesla expand aggressively in India in 2026?"
    })

    print("\n=== LANGGRAPH FINAL DECISION ===")
    print(result["final_decision"])
