from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def finance_agent(research_data: dict):

    prompt = f"""
You are a Financial Impact Analysis Agent.

Using the research data below, analyze financial implications of expansion.

Return ONLY valid JSON.
No markdown.
No explanation.
No backticks.

JSON schema:

{{
  "market_opportunity": "",
  "investment_required": "",
  "revenue_potential": "",
  "cost_considerations": "",
  "roi_outlook": ""
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
        print("⚠️ Finance Agent JSON parsing failed.")
        print(raw_output)
        return raw_output
