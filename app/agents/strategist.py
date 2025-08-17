from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


# Initialize the LLM for the strategist
# We use a more powerful model for the final synthesis to ensure high-quality output.
llm = ChatGroq(
    model="groq/deepseek-r1-distill-llama-70b",
    temperature=0.3 # A slightly higher temperature for more nuanced writing
)

# --- Senior Strategist Agent ---
# This agent synthesizes the findings from other agents into a final report.

strategist_agent = Agent(
    role="Senior Business Strategist", # type: ignore
    goal=(
        "Synthesize the market research and financial analysis into a comprehensive "
        "strategic report. Your report must include a SWOT analysis (Strengths, Weaknesses, "
        "Opportunities, Threats) and a final recommendation for the company's "
        "strategic direction in the specified market."
    ),
    backstory=(
        "You are a highly experienced business strategist who has advised numerous "
        "Fortune 500 companies. You excel at seeing the bigger picture, connecting "
        "disparate data points from market trends and financial reports to craft "
        "a compelling and actionable strategic narrative. Your SWOT analyses are "
        "legendary for their clarity and foresight."
    ),
    tools=[], # This agent synthesizes existing data and doesn't need external tools.
    llm=llm,
    verbose=True,
    allow_delegation=False # Can delegate back to other agents for clarification if needed.
)
