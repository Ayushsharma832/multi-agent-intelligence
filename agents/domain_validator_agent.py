from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def domain_validator_agent(query: str):

    prompt = f"""
You are a domain classifier.

Determine if the following query is related to business, corporate strategy,
market expansion, financial decision, or enterprise analysis.

Return ONLY valid JSON.
No markdown.
No explanation.

JSON schema:
{{
  "is_business_query": true/false,
  "reason": "short explanation"
}}

Query:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw_output = response.choices[0].message.content.strip()

    try:
        return json.loads(raw_output)
    except:
        return {
            "is_business_query": False,
            "reason": "Could not confidently classify query."
        }

