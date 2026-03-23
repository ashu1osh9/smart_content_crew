from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

# Agent 1: Researcher
researcher = Agent(
    role='Senior Research Analyst',
    goal='Kisi bhi topic par internet se latest aur accurate information dhundo',
    backstory="""Tum ek experienced researcher ho jo complex topics ko 
    asaani se samajh lete ho aur best sources dhundhte ho.""",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

# Agent 2: Blog Writer
writer = Agent(
    role='Content Writer',
    goal='Research ke basis par engaging aur SEO-friendly blog post likho',
    backstory="""Tum ek talented writer ho jo technical topics ko 
    simple aur interesting tarike se explain karte ho.""",
    verbose=True,
    allow_delegation=False
)
