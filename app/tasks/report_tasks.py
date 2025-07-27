from crewai import Task
from app.agents import strategist_agent

# --- Final Report Task ---
# This task is for the Senior Strategist Agent. It requires the context
# from both the market research and financial analysis tasks to be completed first.

final_report_task = Task(
    description=(
        "Synthesize the provided market analysis and financial analysis reports "
        "for '{company}' in the '{market}' market. Your primary goal is to create a "
        "single, cohesive, and professional strategic report. "
        "The report must begin with a high-level executive summary. "
        "It must include a detailed SWOT analysis (Strengths, Weaknesses, Opportunities, Threats). "
        "Finally, conclude with a strategic recommendation on whether the company should "
        "expand, maintain its position, or pivot its strategy in this market. "
        "The current date is {current_date}."
    ),
    expected_output=(
        "A comprehensive strategic report in Markdown format. The report must contain:\n"
        "1. **Executive Summary:** A brief overview of the key findings and recommendation.\n"
        "2. **Market Analysis Summary:** Key insights from the market research.\n"
        "3. **Financial Health Summary:** Key insights from the financial analysis.\n"
        "4. **SWOT Analysis:**\n"
        "   - **Strengths:** Internal factors that give the company an advantage.\n"
        "   - **Weaknesses:** Internal factors that are disadvantages.\n"
        "   - **Opportunities:** External factors the company can exploit.\n"
        "   - **Threats:** External factors that could harm the company.\n"
        "5. **Strategic Recommendation:** A clear, actionable recommendation for the company."
    ),
    agent=strategist_agent,
    # This task will be given the outputs of the other tasks as context.
    # It does not execute asynchronously as it must wait for its inputs.
    async_execution=False
)
