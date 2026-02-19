from groq import Groq
import os
from dotenv import load_dotenv
from tavily import TavilyClient
import json
import re


tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

import json

def general_agent(query: str):

    needs_search = False
    context = ""

    # Step 1: Decide if search needed
    decision_prompt = f"""
    Determine if the query requires up-to-date, recent, or future information.
    If it includes a year beyond 2023, current trends, rankings, statistics, or latest data,
    set needs_search to true.

    Return JSON only, with no extra text:
    {{
    "needs_search": true/false
    }}


Query:
{query}
"""

    try:
        decision = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": decision_prompt}],
            temperature=0
        )

        decision_json = json.loads(
            decision.choices[0].message.content.strip()
        )

        needs_search = decision_json.get("needs_search", False)

    except Exception as e:
        needs_search = False
        print("Error in decision prompt:", e)

    # Step 2: Web search if needed
    if needs_search:
        try:
            search_result = tavily_client.search(query=query, max_results=3)
            context = str(search_result.get("results", []))
        except:
            context = ""

    # Step 3: Generate structured answer
    final_prompt = f"""
You are a structured reasoning AI assistant.

Use the following context if provided:
{context}

Return STRICT JSON:
{{
  "summary": "brief overview",
  "key_points": ["point 1", "point 2", "point 3"],
  "recommendation": ["action 1", "action 2"],
  "confidence_level": "Low/Medium/High"
}}


Query:
{query}
"""
    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": final_prompt}],
    temperature=0
)

    raw_output = response.choices[0].message.content.strip()

    try:
        # Extract JSON block using regex
        json_match = re.search(r'\{.*\}', raw_output, re.DOTALL)
        
        if json_match:
            structured = json.loads(json_match.group())
        else:
            raise ValueError("No JSON found")

    except Exception as e:
        structured = {
            "summary": "Response generated without proper structure.",
            "key_points": raw_output,
            "recommendation": "Use discretion.",
            "confidence_level": "Low"
        }


    # 🔥 Always return consistent format
    return {
        "response": structured,
        "used_web_search": needs_search
    }


