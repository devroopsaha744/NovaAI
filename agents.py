import os
from crewai import Agent
from langchain_groq import ChatGroq
from tools import web_search_tool, net_search_tool, scrape_tool
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
chat = ChatGroq(model = "mixtral-8x7b-32768", api_key = groq_api_key)

#Creating a Problem Researcher Agent
researcher = Agent(
    role = "Coding Problem Researcher",
    goal = "Fetch all the important coding questions to practice on the basis of the coding platform profiles give as input",
    backstory = "You are an expert Problem researcher and setter. You analyse the coding platform profiles like Leetcode or Codechef profiles of the user and suggest and fetch all the important coding problems for them to practice",
    tools = [scrape_tool, web_search_tool],
    llm = chat,
    allow_delegation = True
)

#Creating a coding Problem Writer Agent
writer = Agent(
    role = "Coding Problem Writer",
    goal = "Write and list the relevant coding problems you have researched or fetched",
    backstory = "Your job is to jot down or list all the relevannt coding problems that have been fetched or researched according to th user's leetcode or  codechef profie",
    tools = [scrape_tool, web_search_tool],
    llm = chat,
    allow_delegation = False,
)