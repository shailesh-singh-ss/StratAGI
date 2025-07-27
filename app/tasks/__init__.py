# This file makes the 'tasks' directory a Python package.
# It allows us to easily import our defined tasks into the main crew assembly file.

from .market_tasks import market_analysis_task
from .financial_tasks import financial_analysis_task
from .report_tasks import final_report_task

print("Tasks package initialized.")
