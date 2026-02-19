from agents.research_agent import research_agent
from agents.risk_agent import risk_agent
from agents.finance_agent import finance_agent
from agents.strategy_agent import strategy_agent
from agents.synthesizer_agent import synthesizer_agent


class DecisionOrchestrator:

    def __init__(self, query: str):
        self.query = query
        self.state = {}

    def run_research(self):
        self.state["research"] = research_agent(self.query)

    def run_risk_analysis(self):
        self.state["risk"] = risk_agent(self.state["research"])

    def run_financial_analysis(self):
        self.state["finance"] = finance_agent(self.state["research"])

    def run_strategy(self):
        self.state["strategy"] = strategy_agent(
            self.state["research"],
            self.state["risk"],
            self.state["finance"]
        )

    def run_synthesis(self):
        self.state["final_decision"] = synthesizer_agent(
            self.state["risk"],
            self.state["finance"],
            self.state["strategy"]
        )

    def execute(self):
        self.run_research()
        self.run_risk_analysis()
        self.run_financial_analysis()
        self.run_strategy()
        self.run_synthesis()

        return self.state
