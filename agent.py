from langchain_groq import ChatGroq
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from dotenv import load_dotenv

load_dotenv()

def search_topic(topic: str) -> list[str]:
    wrapper = DuckDuckGoSearchAPIWrapper(max_results=8, region="wt-wt")
    queries = [
        topic,
        f"{topic} history and background",
        f"{topic} details and specifications",
        f"{topic} latest news and updates",
    ]
    results = []
    for query in queries:
        try:
            result = wrapper.run(query)
            if result:
                results.append(f"Search: '{query}'\n{result}")
        except Exception:
            continue
    return results

def run_research(topic: str) -> str:
    search_results = search_topic(topic)

    if not search_results:
        return "Could not find any search results. Please try a different topic."

    combined = "\n\n---\n\n".join(search_results)

    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.4)

    prompt = f"""You are an expert research assistant. Based ONLY on the search results below, write a detailed and comprehensive research report about: {topic}

SEARCH RESULTS:
{combined}

Write a detailed report with these sections. Use only information from the search results above.

## Overview
Write 3-4 paragraphs covering background and context.

## Key Findings
Write at least 6 detailed bullet points with specific facts, numbers, and details from the search results.

## Deep Dive
Write 2-3 paragraphs exploring the most interesting aspects in detail.

## Conclusion
Write 1-2 paragraphs summarizing the findings and your analysis.

Important: Be detailed and thorough. The report should be at least 600 words."""

    response = llm.invoke(prompt)
    return response.content
