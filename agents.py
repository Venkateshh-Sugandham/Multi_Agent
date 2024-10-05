from crewai import Agent
from crewai_tools import SerperDevTool
from yt_search_tool import YoutubeVideoSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

# Instantiate the tools
serper_tool = SerperDevTool()  # Create an instance of SerperDevTool
youtube_tool = YoutubeVideoSearchTool()  # Create an instance of YoutubeVideoSearchTool

## Create a senior blog content researcher
research_manager = Agent(
    role="Research Manager",
    goal="""Generate a list of JSON objects containing the URLs for 3 recent blog articles and 
                the URLs and titles for 3 recent YouTube videos for each technology.
                Important: Do not generate fake information. Only return the information you find. Nothing else!""",
    backstory="""As a Research Manager, you are responsible for aggregating all the researched information into a list.""",
    verbose=True,
    memory=True,
    tools=[youtube_tool,serper_tool],
    allow_delegation=True
)

## Create a senior blog writer agent with YouTube tool
research_agent = Agent(
    role="Research Agent",
    goal="""Look up the specified technology and find URLs for 3 recent blog articles and 
                the URLs and titles for 3 recent YouTube videos related to the technology. It is your goal to return this collected 
                information in a JSON object.""",
    verbose=False,
    memory=True,
    backstory="""As a Research Agent, you are responsible for looking up the specified technology and gathering relevant information.
                
                Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                """,
    tools=[youtube_tool,serper_tool],
    allow_delegation=False
)

