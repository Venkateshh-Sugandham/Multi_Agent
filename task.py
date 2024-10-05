from crewai import Task
from crewai_tools import SerperDevTool
from yt_search_tool import YoutubeVideoSearchTool
from textwrap import dedent
from agents import research_manager, research_agent
from models import Results



# Instantiate the tools
serper_tool = SerperDevTool()  # Create an instance of SerperDevTool
youtube_tool = YoutubeVideoSearchTool()  # Create an instance of YoutubeVideoSearchTool

## Research Task
research_task = Task(
    description=dedent("""Based on the input topic '{topic}',
                Find the URLs and titles for 3 recent blog articles and the URLs and titles for
                3 recent YouTube videos in this topic.
                Return this collected information in a JSON object.
                
                Helpful Tips:
                - To find the blog articles names and URLs, perform searches on Google such as:
                    - "{topic} blog articles"
                - To find the YouTube videos, perform searches on YouTube such as:
                    - "{topic} latest videos"
                
                Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find.
                - Do not stop researching until you find the requested information for this topic.
                """),
    expected_output=dedent(
                """A JSON object containing the researched information (titles and URLs) for the topic."""),  # Update expected output
    agent=research_agent,  # Ensure agent is updated for this task
    tools=[youtube_tool, serper_tool]  # No changes needed here
)

# Writing task with language model configuration
write_task = Task(
    description=dedent(
        """Based on the input topic '{topic}', 
                use the results from the Research Agent to research and
                put together a JSON object containing the titles and URLs for 3 blog articles, 
                and the titles and URLs for 3 YouTube videos trending in this topic.
                """),
    expected_output=dedent(
                """A CSV output containing the titles and URLs for 3 blog articles and the titles and URLs for 
                    3 YouTube videos trending in this topic."""),  # Ensure titles are mentioned
    output_json=Results,  # Should use the updated Results model with NamedUrl
    agent=research_manager,  # Ensure agent is responsible for this task
    tools=[youtube_tool, serper_tool],  # No changes needed here
    async_execution=True,
)