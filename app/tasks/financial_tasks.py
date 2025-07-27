from crewai import Task
from app.agents import financial_analyst_agent

# --- Financial Analysis Task ---
# This task instructs the Financial Analyst agent to analyze the company's
# financial health using the data retrieved from its tools.

financial_analysis_task = Task(
    description=(
        "Analyze the financial health of the company '{company}'. "
        "Use the company's stock ticker symbol to fetch the latest financial data. "
        "Your analysis should provide a clear overview of the company's valuation, "
        "profitability, and key financial ratios. "
        "Incorporate the market analysis context to assess if the company's financial "
        "performance aligns with market trends."
    ),
    expected_output=(
        "A concise financial report including:\n"
        "1. A summary of the company's key financial metrics (Market Cap, P/E Ratio, EPS).\n"
        "2. An analysis of the company's financial strengths and weaknesses.\n"
        "3. A concluding statement on the company's overall financial health."
    ),
    agent=financial_analyst_agent,
    async_execution=True
)
