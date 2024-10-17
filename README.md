# Multi_Agent
AI agent using Python and Crew AI to automate the search process for  relevant blog articles and YouTube videos on a given topic. The system utilized tools like  SerperDevTool for web scraping and YouTube Search Tool for video retrieval


## Technologies Used- **Python**: Core programming language used for the project.
- **Crew AI**: Used for defining and managing AI agents and tasks.
- **Langchain**: Provides the ability to manage natural language processing workflows and agent-based tasks.
- **SerperDevTool**: Used for web scraping to find relevant blog articles.
- **YouTube API**: Utilized for retrieving YouTube videos based on search queries.
- **Pydantic**: Ensures data validation and serialization in JSON format.
- **Streamlit**: Simple UI for inputting topics and displaying search results.

## Installation
### Clone this repository:

```
git clone https://github.com/Venkateshh-Sugandham/Multi_Agent.git
cd Multi_Agent
```
### Create a Virtual Environment
```
python3 -m venv venv
```
### Activate the Virtual Environment
```
venv\Scripts\activate
```

### Install the required dependencies:
```
pip install -r requirements.txt
```
### Create a .env file in the root directory and add your API keys for YouTube and SerperDevTool:
```
YOUTUBE_API_KEY=your_youtube_api_key
SERPER_API_KEY=your_serper_api_key
```
### Running the Application
```
streamlit run app.py
```
Enter the topic of interest in the app's input field, and the system will automatically retrieve and display the relevant blog articles and YouTube videos.

