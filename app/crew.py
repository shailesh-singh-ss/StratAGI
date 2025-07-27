import os
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process

# Load environment variables from the .env file
load_dotenv()

# Import all agents and tasks
from app.agents import market_researcher_agent, financial_analyst_agent, strategist_agent
from app.tasks import market_analysis_task, financial_analysis_task, final_report_task

class StratAGICrew:
    """
    A class to manage the assembly and execution of the StratAGI crew.
    """
    def __init__(self, company: str, market: str):
        self.company = company
        self.market = market

    def run(self):
        """
        Assembles the crew with dynamic tasks and kicks off the analysis process.
        """
        # Set the context for the final report task.
        # This tells the strategist_agent to use the output of the other two tasks.
        final_report_task.context = [market_analysis_task, financial_analysis_task]

        # Assemble the crew with a sequential process
        crew = Crew(
            agents=[
                market_researcher_agent,
                financial_analyst_agent,
                strategist_agent
            ],
            tasks=[
                market_analysis_task,
                financial_analysis_task,
                final_report_task
            ],
            process=Process.sequential,  # Ensures tasks are executed one after another
            verbose=True  # Logs the execution process for transparency
        )

        # Prepare the inputs for the crew's kickoff
        inputs = {
            "company": self.company,
            "market": self.market,
            "current_date": datetime.now().strftime("%Y-%m-%d")
        }

        # Kick off the crew's work and return the final result
        result = crew.kickoff(inputs=inputs)
        return result

# This block allows for direct execution of the crew for testing purposes
if __name__ == '__main__':
    print("--- Running StratAGI Crew for Testing ---")
    company_to_analyze = "Tesla"
    market_to_analyze = "Indian Electric Vehicle market"
    
    stratagi_crew = StratAGICrew(company_to_analyze, market_to_analyze)
    final_result = stratagi_crew.run()
    
    print("\n\n--- StratAGI Crew Finished ---")
    print("Final Report:")
    print(final_result)
