import os
from dotenv import load_dotenv
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

load_dotenv()
serp_api_key = os.getenv("SERPER_API_KEY")

#Tool to enable searching
net_search_tool = SerperDevTool()



