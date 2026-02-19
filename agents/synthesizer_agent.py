from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def synthesizer_agent(risk_data: dict, finance_data: dict, strategy_data: dict):

    prompt = f"""
You are a Decision Intelligence Synthesizer.

Using the structured inputs below:

Risk Analysis:
{risk_data}

Financial Analysis:
{finance_data}

Strategy Recommendation:
{strategy_data}

Provide a final executive decision.

Return ONLY valid JSON.
No markdown.
No explanation.
No backticks.

JSON schema:

{{
  "final_decision": "Go / Conditional Go / No-Go",
  "justification_summary": "",
  "key_monitoring_metrics": ""
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
        print("⚠️ Synthesizer Agent JSON parsing failed.")
        print(raw_output)
        return raw_output
