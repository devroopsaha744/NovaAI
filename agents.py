import os
from crewai import Agent
from langchain_groq import ChatGroq
from tools import web_search_tool
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
chat = ChatGroq(model = "mixtral-8x7b-32768", api_key = groq_api_key)

#Creating a Blog Researcher Agent
researcher = Agent(
    role = "Blog Researcher",
    goal = "Research and Fetch all the relevant and important content from authentic resources about the topic:{topic} given as input.",
    backstory = "You are an expert researcher. You will research anb fetch all the relevant content about the given topic :  {topic} from authentic resources",
    tools = [web_search_tool],
    llm = chat,
    allow_delegation = True
)

#Creating a Blog Writer Agent
writer = Agent(
    role = "Blog Writer",
    goal = "Write a compreshensive blog or a doc about the topic: {topic}. The doc/Blog should be very detailed with headings, subheadings and all and also put refernces/bibliogrpahy at the end.",
    backstory = "You are an expert writer. You will write a comprehensive doc or a blog about the topic: {topic} that has been researched along with headings, subheadings and all. Also add refernces/bibliography at the end.  ",
    tools = [web_search_tool],
    llm = chat,
    allow_delegation = False,
)