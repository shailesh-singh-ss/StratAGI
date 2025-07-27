from crewai import Task
from app.agents import market_researcher_agent

# --- Market Analysis Task ---
# This task directs the Market Researcher agent to perform a deep dive
# into the company's market positioning and the overall industry trends.

market_analysis_task = Task(
    description=(
        "Investigate the company '{company}' in the '{market}' market. "
        "Your primary goal is to analyze the latest market trends, news, and competitive landscape. "
        "Focus on identifying key growth drivers, potential challenges, and major competitors. "
        "Provide a concise yet comprehensive summary of your findings, highlighting the most critical insights."
    ),
    expected_output=(
        "A detailed report summarizing the market analysis. The report should include:\n"
        "1. An overview of the current market trends in the '{market}' industry.\n"
        "2. A summary of recent significant news related to '{company}'.\n"
        "3. A list of key competitors with a brief analysis of their market position.\n"
        "4. A summary of potential opportunities and threats for '{company}' in this market."
    ),
    agent=market_researcher_agent,
    # Allowing asynchronous execution to improve performance
    async_execution=True
)
