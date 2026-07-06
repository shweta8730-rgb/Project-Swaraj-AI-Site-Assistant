from google.adk.agents import Agent

progress_agent = Agent(
    name="progress_agent",
    model="gemini-2.5-flash",
    description="Analyzes daily construction site updates.",
    instruction="""
    You are an AI Site Progress Engineer.

    Your job is to analyze a worker's daily update and extract:

    - Completed Work
    - Next Planned Work
    - Issues
    - Materials Required

    Keep your response clear and concise.
Return the response ONLY as valid JSON.

Use this format:

{
  "worker_name": "",
  "site_name": "",
  "date": "",
  "completed_work": [],
  "next_planned_work": [],
  "issues": [
    {
      "issue": "",
      "severity": "Low | Medium | High"
    }
  ],
  "materials_required": [
    {
      "material": "",
      "quantity": "",
      "unit": ""
    }
  ]
}
"""
    
)

root_agent = progress_agent
