# This file is reserved for custom browser or search-related tools.
# For our primary web search functionality, we will be using the pre-built
# `BraveSearchTool` tool from the `crewai_tools` library.
#
# This tool is highly effective and directly integrates with CrewAI.
# We will instantiate it directly within our agent definitions.
#
# Example of a custom tool that could be added here later:
# - A tool to scrape a specific website's content using BeautifulSoup.
# - A tool to interact with a specific API like Wikipedia.

import os
import json
import requests
from crewai.tools import BaseTool
from tavily import TavilyClient


class CustomTavilySearchTool(BaseTool):
    name: str = "Custom Tavily Search Tool"
    description: str = (
        "A custom tool to perform web searches using the Tavily API. "
        "Use this to get up-to-date information from the internet. "
        "Input should be a single search query string."
    )

    def _run(self, query: str) -> str:
        """
        Executes the search using a direct call to the Tavily API.
        """
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "Error: TAVILY_API_KEY environment variable not set."

        tavily_client = TavilyClient(api_key)

        try:
            response = tavily_client.search(query=query, num_results=5, include_answer=True)
            
            results = response.get('results', [])
            if not results:
                return "No results found for the query."
            
            # Format the results into a readable string
            formatted_results = [f"answer: {response.get('answer', 'No answer provided')}"]
            for res in results:
                formatted_results.append(
                    f"- Title: {res.get('title', 'N/A')}\n"
                    f"  URL: {res.get('url', 'N/A')}\n"
                    f"  Snippet: {res.get('content', 'N/A')}\n"
                )
            return "\n".join(formatted_results)

        except requests.exceptions.RequestException as e:
            return f"An error occurred while calling Tavily API: {e}"
        except Exception as e:
            return f"An unknown error occurred: {e}"



if __name__ == "__main__":
    # Example usage of the CustomTavilySearchTool
    tool = CustomTavilySearchTool()
    query = "latest trends in AI technology"
    result = tool._run(query)
    print(result)  # This will print the formatted search results or an error message.