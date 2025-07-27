import os
from crewai import Agent, LLM
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from app.tools.browser_tools import CustomTavilySearchTool
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()


# Initialize the LLM
# We use Groq for its speed and access to powerful open-source models.
llm = ChatGroq(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.1 # Lower temperature for more factual, less creative output
)

# Initialize the Google Generative AI model
llm_google = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.1
)

# --- Market Researcher Agent ---
# This agent is designed to be an expert in finding and summarizing
# information from the web.

market_researcher_agent = Agent(
    role="Expert Market Researcher",
    goal=(
        "Find and analyze the latest market trends, news, and competitive landscape "
        "for a given company and its industry. Provide a concise summary of key findings."
    ),
    backstory=(
        "As a seasoned market researcher, you have a keen eye for impactful news and "
        "a knack for distilling vast amounts of information into actionable insights. "
        "You are an expert at using online search tools to uncover data that others might miss, "
        "focusing on market size, growth drivers, and competitive dynamics."
    ),
    tools=[CustomTavilySearchTool()],
    llm=llm_google,
    verbose=True,
    allow_delegation=False,
    max_iter=5
)

