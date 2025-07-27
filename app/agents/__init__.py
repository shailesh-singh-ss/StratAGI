# This file makes the 'agents' directory a Python package.
# It allows us to easily import our defined agents into other parts of the application,
# such as the main crew assembly file.

from .market_researcher import market_researcher_agent
from .financial_analyst import financial_analyst_agent
from .strategist import strategist_agent

print("Agents package initialized.")

