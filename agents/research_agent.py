from tools.search_tool import web_search
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def research_agent(user_query: str):
    search_results = web_search(user_query)

    combined_content = "\n\n".join(
        [f"{r['title']}\n{r['content']}" for r in search_results]
    )

    prompt = f"""
You are a Research Agent.

Using the web search results below, extract structured insights.

Return ONLY valid JSON.
Do NOT include markdown.
Do NOT include explanation.
Do NOT include backticks.
Do NOT include notes.

JSON schema:

{{
  "market_trends": "",
  "competitors": "",
  "regulatory_environment": "",
  "recent_news": ""
}}

Web Data:
{combined_content}
"""


    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    import json
    raw_output = response.choices[0].message.content.strip()

    try:
        structured_output = json.loads(raw_output)
        return structured_output
    except:
        print("⚠️ JSON parsing failed.")
        print(raw_output)
        return raw_output
