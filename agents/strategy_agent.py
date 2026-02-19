from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def strategy_agent(research_data: dict, risk_data: dict, finance_data: dict):

    prompt = f"""
You are a Strategy Formulation Agent.

Using the following structured inputs:

Research Data:
{research_data}

Risk Analysis:
{risk_data}

Financial Analysis:
{finance_data}

Provide a strategic recommendation.

Return ONLY valid JSON.
No markdown.
No explanation.
No backticks.

JSON schema:

{{
  "strategic_options": "",
  "recommended_strategy": "",
  "execution_roadmap": "",
  "confidence_level": "Low/Medium/High"
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw_output = response.choices[0].message.content.strip()

    try:
        structured_output = json.loads(raw_output)
        return structured_output
    except:
        print("⚠️ Strategy Agent JSON parsing failed.")
        print(raw_output)
        return raw_output
