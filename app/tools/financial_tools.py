import os
from crewai.tools import BaseTool
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Tool for fetching Company Overview from Alpha Vantage ---
# This tool retrieves fundamental data for a given company stock symbol.
# It's essential for the Financial Analyst agent to understand the company's health.

class CompanyOverviewTool(BaseTool):
    name: str = "Company Overview Tool"
    description: str = (
        "Retrieves a comprehensive overview of a public company from Alpha Vantage, "
        "including key financial ratios, valuation metrics, and business summary. "
        "Input should be a single company stock ticker symbol (e.g., 'TSLA')."
    )

    def _run(self, ticker_symbol: str) -> str:
        """
        Executes the tool to fetch company overview data.
        """
        api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
        if not api_key:
            return "Error: ALPHA_VANTAGE_API_KEY environment variable not set."
        
        url = os.getenv("ALPHA_VANTAGE_URL")
        if not url:
            return "Error: ALPHA_VANTAGE_URL environment variable not set."
        
        # Prepare the parameters for the API request
        PARAMS = {
            "function": "OVERVIEW",
            "symbol": ticker_symbol,
            "apikey": api_key
        }

        try:
            
            # Fetch the company overview data
            overview_data = requests.get(url, params=PARAMS).json()

            if not overview_data:
                return f"Error: No data found for ticker symbol '{ticker_symbol}'. It might be an invalid symbol."

            # We can select and format the most important pieces of information
            # to return a clean, concise summary for the agent.
            formatted_summary = self.format_summary(overview_data)
            
            return formatted_summary

        except Exception as e:
            return f"An error occurred while fetching data from Alpha Vantage: {e}"

    def format_summary(self, data: dict) -> str:
        """
        Formats the raw JSON data into a more readable string summary.
        """
        # Selecting key metrics to present to the agent
        key_metrics = {
            "Company Name": data.get("Name"),
            "Description": data.get("Description"),
            "Industry": data.get("Industry"),
            "Market Capitalization": f"${int(data.get('MarketCapitalization', 0)):,}",
            "P/E Ratio": data.get("PERatio"),
            "EPS": data.get("EPS"),
            "52 Week High": data.get("52WeekHigh"),
            "52 Week Low": data.get("52WeekLow"),
            "Analyst Target Price": data.get("AnalystTargetPrice"),
        }
        
        summary = "Company Financial Overview:\n"
        for key, value in key_metrics.items():
            if value: # Only include fields that have data
                summary += f"- {key}: {value}\n"
        
        return summary


if __name__ == "__main__":
    # Example usage of the tool
    tool = CompanyOverviewTool()
    print(tool._run("IBM"))  