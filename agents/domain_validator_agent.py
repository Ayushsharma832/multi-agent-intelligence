from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def domain_validator_agent(query: str):

    prompt = f"""
Classify the intent of the following query.

Return ONLY JSON.
No explanation outside JSON.

JSON schema:
{{
  "intent": "strategic" | "informational" | "general",
  "reason": "short explanation"
}}

Definitions:

strategic → Business strategy, investment decisions, corporate expansion, risk evaluation.

informational → Requests for facts, statistics, rankings, current data, economic indicators.

general → Personal advice, lifestyle questions, philosophical or casual questions.

Query:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    import re

    def safe_json_extract(text):
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return match.group()
        return None
        
    raw_output = response.choices[0].message.content.strip()
    cleaned = safe_json_extract(raw_output)
    try:
        return json.loads(cleaned)
    except:
        return {
            "intent": "general",
            "reason": "Model output was not valid JSON."
        }

