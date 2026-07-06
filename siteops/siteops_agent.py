from google.adk.agents import Agent

from .progress_agent import progress_agent
from .summary_agent import summary_agent

siteops_agent = Agent(
    name="siteops_agent",
    model="gemini-2.5-flash",
    description="Manages construction site operations.",
    instruction="""
You are the Site Operations Manager.

You have two specialist agents:

1. Progress Agent
   - Extracts structured JSON from worker updates.

2. Summary Agent
   - Creates the daily summary from worker reports.

Use the correct agent depending on the user's request.
""",
    sub_agents=[
        progress_agent,
        summary_agent,
    ]
)

root_agent = siteops_agent