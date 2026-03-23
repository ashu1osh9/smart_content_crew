from crewai import Task
from agents import researcher, writer

def create_tasks(topic):
    # Task 1: Research
    research_task = Task(
        description=f"""
        Is topic par detailed research karo: {topic}
        
        Ye cover karo:
        - Latest developments
        - Key statistics
        - Important examples
        - Expert opinions
        """,
        expected_output="Comprehensive research report in bullet points",
        agent=researcher
    )

    # Task 2: Write Blog
    write_task = Task(
        description=f"""
        Research ke basis par {topic} par ek engaging blog post likho.
        
        Include karo:
        - Catchy title
        - Introduction
        - Main sections with headings
        - Conclusion
        - Minimum 800 words
        """,
        expected_output="Full blog post in Markdown format",
        agent=writer,
        context=[research_task]
    )

    return [research_task, write_task]
