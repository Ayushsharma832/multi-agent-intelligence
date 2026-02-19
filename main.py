from orchestrator import DecisionOrchestrator

if __name__ == "__main__":
    query = "Should Tesla expand aggressively in India in 2026?"

    orchestrator = DecisionOrchestrator(query)
    result = orchestrator.execute()

    print("\n=== FINAL DECISION REPORT ===")
    print(result["final_decision"])
