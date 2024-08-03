from crewai import Task
from agents import researcher, writer
from tools import scrape_tool, web_search_tool

research = Task(
    description = [
        "Analyse, research and Fetch all the important Coding problems from differnet platforms related to the {topic} and {difficulty}",
        "search and fetch relevant coding questions for the user to improve there DSA skills"
    ],
    expected_output = "a comprehensive list of the coding problems relevant for the user so that the user can practice the problems listed here and can improve their coding skills",
    agent = researcher,
    tools = [scrape_tool, web_search_tool]
)

write = Task(
    description = [
        "Jot down a comprehensive list of coding problems that are relevant for the user based the user's leetcode profile {profile}",
        "List down and write up those coding questions that the user can practice to improve there Leetcode and DSA skills ",
    ],
    expected_output = "a comprehensive list of the coding problems relevant for the user so that the user can practice the problems listed here and can improve their coding skill",
    agent = writer,
    async_execution = False,
    output_file = "analysis.md"
)

