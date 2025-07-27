StratAGI: The Autonomous Business Strategy Analyst
StratAGI is a fully deployed, multi-agent AI system that performs comprehensive business and market analysis on demand. A user can input a company name and a target market, and StratAGI autonomously deploys a team of specialized AI agents to research, analyze, and synthesize a professional-grade strategic report.

Live Demo: [Link to be added upon deployment]

(A proper architecture diagram will be created and added here)

✨ Core Features
Autonomous Planning & Decomposition: Takes a high-level goal and breaks it down into executable sub-tasks.

Multi-Agent Collaboration: Specialized agents collaborate, passing data and refining work to solve complex problems.

Dynamic Tool Use: Agents intelligently select and use the right tool for the job (e.g., web search for news, financial data APIs).

Structured Output: The system culminates in a structured, professional report, not just a simple text response.

🛠️ Tech Stack & Architecture
This project is built with a modern, open-source-first stack, designed for scalability and relevance in the current AI landscape.

Agentic Framework: CrewAI - Chosen for its clear, role-based structure that maps perfectly to our agent team concept.

LLMs: Groq with Llama3/Mixtral. We will use the Groq API for lightning-fast inference on powerful open-source models, which offers a generous free tier.

Backend: FastAPI - A high-performance Python framework for building our API endpoint.

Frontend: Streamlit - The fastest way to build a beautiful, data-centric web app purely in Python.

Tooling & APIs:

Web Search: Tavily AI API - A search API optimized for AI agents, with a free plan for initial development.

Financial Data: Alpha Vantage API - The standard for free, comprehensive financial and stock market data.

Deployment:

Containerization: Docker - To package our application and its dependencies for consistent deployment.

Hosting: Streamlit Community Cloud / Hugging Face Spaces - Excellent free options for deploying Streamlit applications.

🚀 Project Structure
stratagi-analyst/
├── .github/
│   └── workflows/
│       └── cicd.yml         # (Optional) CI/CD pipeline
├── app/
│   ├── agents/              # CrewAI Agent definitions
│   │   ├── __init__.py
│   │   ├── financial_analyst.py
│   │   └── market_researcher.py
│   ├── tasks/               # CrewAI Task definitions
│   │   ├── __init__.py
│   │   ├── financial_tasks.py
│   │   └── market_tasks.py
│   ├── tools/               # Custom tool definitions
│   │   ├── __init__.py
│   │   └── browser_tools.py
│   │   └── financial_tools.py
│   ├── main.py              # FastAPI application
│   └── crew.py              # Crew definition and assembly
├── frontend/
│   └── app.py               # Streamlit frontend application
├── .dockerignore
├── .env.example             # Example environment variables
├── Dockerfile               # Dockerfile for deployment
├── README.md                # This file
└── requirements.txt         # Python dependencies

⚙️ Setup and Local Execution
1. Prerequisites
Python 3.9+

An API key from:

Groq

Tavily AI

Alpha Vantage

2. Installation
Clone the repository:

git clone https://github.com/[YOUR_USERNAME]/stratagi-analyst.git
cd stratagi-analyst

Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

Set up environment variables:

Create a .env file in the root directory by copying .env.example.

Add your API keys to the .env file:

GROQ_API_KEY="gsk_..."
TAVILY_API_KEY="tvly-..."
ALPHA_VANTAGE_API_KEY="..."

3. Running the Application
Start the FastAPI backend:

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

In a new terminal, start the Streamlit frontend:

streamlit run frontend/app.py

Open your browser to http://localhost:8501 to use the application.