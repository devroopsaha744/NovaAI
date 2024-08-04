import os
from crewai import Agent
from langchain_groq import ChatGroq
from tools import web_search_tool
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
chat = ChatGroq(model = "mixtral-8x7b-32768", api_key = groq_api_key)

#Creating a Problem Researcher Agent
researcher = Agent(
    role = "Coding Problem Researcher",
    goal = "Fetch all the important coding questions to practice on the basis of the {topic} and {difficulty} given as an input",
    backstory = "You are an expert Problem researcher and setter. You find all the relevant resources and important coding problems (from popular coding websites like Leetcode, GFG, interviewBit, Codeforces, AtCoder etc.) on the basis of the topic given as an input",
    tools = [web_search_tool],
    llm = chat,
    allow_delegation = True
)

#Creating a coding Problem Writer Agent
writer = Agent(
    role = "Coding Problem Writer",
    goal = "Write the tips to solve those problems, explain the different approaches to be taken during problem solving  and list the relevant coding problems you have researched or fetched",
    backstory = "Your job is to jot down or list all the relevannt coding problems, approaches and concepts that have been fetched or researched according to the topic and difficulty given",
    tools = [web_search_tool],
    llm = chat,
    allow_delegation = False,
)