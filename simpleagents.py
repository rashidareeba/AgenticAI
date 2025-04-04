from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    description="You are an assistant please reply based on the question",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("Who won the 1992 worldcup?")

