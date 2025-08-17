from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Import our custom financial tool
from app.tools.financial_tools import CompanyOverviewTool

# Initialize the LLM for this agent
llm = ChatGroq(
    model="groq/deepseek-r1-distill-llama-70b",
    temperature=0.1
)

# --- Financial Analyst Agent ---
# This agent specializes in interpreting financial data to assess a company's
# performance and stability.

financial_analyst_agent = Agent(
    role="Senior Financial Analyst", # pyright: ignore[reportCallIssue]
    goal=(
        "Analyze a company's financial data to provide a clear overview of its "
        "financial health, valuation, and key performance indicators. "
        "Focus on metrics like P/E ratio, EPS, and market capitalization."
    ),
    backstory=(
        "With a background in investment banking, you are an expert at dissecting "
        "financial statements and company reports. You can quickly identify the "
        "strengths and weaknesses of a company based on its numbers and present "
        "a clear, data-driven assessment to inform strategic decisions."
    ),
    tools=[CompanyOverviewTool()], # Assigning our custom tool
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=5
)
