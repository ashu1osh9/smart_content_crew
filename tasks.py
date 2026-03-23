from crewai import Task
from agents import researcher, writer

def create_tasks(topic):
    # Task 1: Research
    research_task = Task(
        description=f"""
        Conduct detailed research on the following topic: {topic}
        
        Make sure to cover:
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
        Using the research provided, write an engaging blog post on: {topic}
        
        Make sure to include:
        - A catchy title
        - Introduction
        - Main sections with clear headings
        - Conclusion
        - Minimum 800 words
        """,
        expected_output="Full blog post in Markdown format",
        agent=writer,
        context=[research_task]
    )

    return [research_task, write_task]
