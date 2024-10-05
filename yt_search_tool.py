from typing import List, Type
from pydantic.v1 import BaseModel, Field  # Adjust based on pydantic version
import os
import requests
from crewai_tools import BaseTool

class VideoSearchResult(BaseModel):
    title: str
    video_url: str

class YoutubeVideoSearchToolInput(BaseModel):
    """Input for YoutubeVideoSearchTool."""
    keyword: str = Field(..., description="The search keyword.")
    max_results: int = Field(10, ge=1, le=50, description="The maximum number of results to return.")  # Enforce max constraint

class YoutubeVideoSearchTool(BaseTool):
    name: str = "Search YouTube Videos"
    description: str = "Searches YouTube videos based on a keyword and returns a list of video search results."
    args_schema: Type[YoutubeVideoSearchToolInput] = YoutubeVideoSearchToolInput  # More explicit type hint

    def _run(self, keyword: str, max_results: int = 10) -> List[VideoSearchResult]:
        api_key = os.getenv("YOUTUBE_API_KEY")
        if not api_key:
            raise ValueError("YouTube API key not found. Please set the YOUTUBE_API_KEY environment variable.")
        
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": keyword,
            "maxResults": max_results,
            "type": "video",
            "key": api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to retrieve data from YouTube API: {e}")

        items = response.json().get("items", [])

        results = []
        for item in items:
            title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            results.append(VideoSearchResult(
                title=title,
                video_url=video_url,
            ))

        return results
