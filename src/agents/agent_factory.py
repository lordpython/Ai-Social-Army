from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from typing import Any, Optional

def create_agent(role: str, backstory: str, goal: str, llm: Any, cache: Optional[None] = None):
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    
    return Agent(
        role=role,
        backstory=backstory,
        goal=goal,
        allow_delegation=False,
        verbose=True,
        max_iter=3,
        max_rpm=20,
        llm=llm,
        tools=[search_tool, scrape_tool],
    )