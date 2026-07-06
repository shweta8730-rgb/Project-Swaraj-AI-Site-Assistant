from google.adk.agents import Agent

summary_agent = Agent(
    name="summary_agent",
    model="gemini-2.5-flash",
    description="Creates a daily site summary from multiple worker updates.",
    instruction="""
    You are an AI Site Supervisor.

    Your job is to read multiple worker progress reports and create a single
    concise daily summary for the site owner.

    Focus on:

    - Overall completed work
    - Work planned for tomorrow
    - Major issues
    - Materials required

    Keep the summary short, clear and easy to read.
    """
)

root_agent = summary_agent