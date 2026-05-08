from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.prompts import PromptTemplate
from tools import get_search_tool
from dotenv import load_dotenv

load_dotenv()

PROMPT_TEMPLATE = """You are a research assistant. Research the topic thoroughly and produce a clear, structured report.

You have access to the following tools:
{tools}

Use this format strictly:
Question: the research topic
Thought: what should I search for?
Action: the action to take, must be one of [{tool_names}]
Action Input: the search query
Observation: the result
... (repeat at least 3 times)
Thought: I have enough information
Final Answer: A structured report with sections: ## Summary, ## Key Findings, ## Conclusion

Begin!

Question: {input}
Thought:{agent_scratchpad}"""

def run_research(topic: str) -> str:
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
    tools = [get_search_tool()]
    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    agent = create_react_agent(llm, tools, prompt)
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=8,
        handle_parsing_errors=True
    )
    result = executor.invoke({"input": f"Research this topic in depth: {topic}"})
    return result["output"]