from crewai import Crew,Process
from agents import research_manager, research_agent
from task import research_task,write_task


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[research_manager, research_agent],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)


