import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query: str):
    response = tavily.search(query=query, search_depth="advanced", max_results=5)
    
    results = []
    for r in response["results"]:
        results.append({
            "title": r["title"],
            "url": r["url"],
            "content": r["content"]
        })
    
    return results
