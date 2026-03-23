from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

# Agent 1: Researcher
researcher = Agent(
    role='Senior Research Analyst',
    goal='Find the latest and most accurate information on any given topic from the internet',
    backstory="""You are an experienced researcher who understands complex topics with ease 
    and always finds the best and most reliable sources.""",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

# Agent 2: Blog Writer
writer = Agent(
    role='Content Writer',
    goal='Write engaging and SEO-friendly blog posts based on the research provided',
    backstory="""You are a talented writer who explains technical topics in a simple, 
    clear, and interesting way that keeps readers hooked.""",
    verbose=True,
    allow_delegation=False
)
