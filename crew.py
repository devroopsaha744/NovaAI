from crewai import Crew,Process
from tasks import research,write
from agents import researcher,writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[researcher,writer],
    tasks=[research,write],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic': "Prefix Sum", 'difficulty':'Easy and Medium'})
print(result)