from crewai import Crew, Process
from agents import researcher, writer
from tasks import create_tasks

def run_crew(topic):
    tasks = create_tasks(topic)

    crew = Crew(
        agents=[researcher, writer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result
