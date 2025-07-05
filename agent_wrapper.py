import os
from agno.agent import Agent
from agno.models.groq import Groq

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment. Please set it in your .env file.")

agent = Agent(
    model=Groq(id="gemma2-9b-it", api_key=api_key),
    description="Analyze user-reported application issues and suggest possible causes.",
    markdown=False,
)

def analyze_issue(issue: str) -> str:
    prompt = f"User reported an issue: '{issue}'. What are 3 possible technical causes?"
    response = agent.run(prompt)

    if hasattr(response, "content") and isinstance(response.content, str):
        return response.content.strip()
    elif isinstance(response, str):
        return response.strip()
    else:
        return str(response).strip()
