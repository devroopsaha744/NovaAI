from crewai import Task
from agents import researcher, writer
from tools import web_search_tool

research = Task(
    description = "Research, fetch and analyse all kinds of content you can get of the mentioned topic : {topic} of course from authentic resources.",
    expected_output= "A comprehesive Blog on the mentioned topic : {topic}, explaining the topic in great detail, along with headings, subheadings and all and also provide bibliography/references at the end.",
    agent = researcher,
    tools = [web_search_tool]
)

write = Task(
    description = "Write a compreshensive blog or a doc about  topic: {topic}. The doc/Blog should be very detailed with headings, subheadings and all and also put refernces/bibliogrpahy at the end.",
    expected_output = "A comprehesive Blog or a document on the mentioned topic: {topic}, explaining the topic in great detail, along with headings, subheadings and all and also provide bibliography/references at the end.",
    agent = writer,
    async_execution = False,
    output_file = "Blog.md"
)

