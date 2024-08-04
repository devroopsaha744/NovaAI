import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

load_dotenv()
serp_api_key = os.getenv("SERPER_API_KEY")

#Tool to enable searching
web_search_tool = SerperDevTool()



