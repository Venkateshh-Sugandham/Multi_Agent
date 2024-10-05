from typing import List
from pydantic import BaseModel, HttpUrl


# Create a class to store both title (name) and URL
class NamedUrl(BaseModel):
    title: str  # Store the title of the blog article or YouTube video
    url: HttpUrl  # Store the URL


# Modify Results class to include NamedUrl instead of just URLs
class Results(BaseModel):
    topic: str
    blog_articles_urls: List[NamedUrl]  # List of blog articles with titles and URLs
    youtube_videos_urls: List[NamedUrl]  # List of YouTube videos with titles and URLs


class ResultsList(BaseModel):
    Output: List[Results]
