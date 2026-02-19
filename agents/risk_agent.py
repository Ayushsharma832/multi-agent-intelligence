from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def risk_agent(research_data: dict):

    prompt = f"""
You are a Risk Analysis Agent.

Based on the research data below, analyze strategic risks.

Return ONLY valid JSON.
No markdown.
No explanation.
No backticks.

JSON schema:

{{
  "political_risk": "Low/Medium/High",
  "regulatory_risk": "Low/Medium/High",
  "competitive_risk": "Low/Medium/High",
  "economic_risk": "Low/Medium/High",
  "overall_risk_score": "Integer between 1 and 100"
}}


Research Data:
{research_data}
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
        print("⚠️ Risk Agent JSON parsing failed.")
        print(raw_output)
        return raw_output
