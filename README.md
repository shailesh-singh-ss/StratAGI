# StratAGI: The Autonomous Business Strategy Analyst

[![GitHub Stars](https://img.shields.io/github/stars/shailesh-singh-ss/StratAGI?style=social)](https://github.com/shailesh-singh-ss/StratAGI)
[![GitHub Forks](https://img.shields.io/github/forks/shailesh-singh-ss/StratAGI?style=social)](https://github.com/shailesh-singh-ss/StratAGI)
[![License](https://img.shields.io/github/license/shailesh-singh-ss/StratAGI)](https://github.com/shailesh-singh-ss/StratAGI/blob/main/LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

StratAGI is a fully deployed, multi-agent AI system that performs comprehensive business and market analysis on demand. A user can input a company name and a target market, and StratAGI autonomously deploys a team of specialized AI agents to research, analyze, and synthesize a professional-grade strategic report.

## 🌟 Live Demo

**[Coming Soon]** - Live demo will be available upon deployment

## 📊 Architecture Overview

```
┌─────────────────┐     ┌─────────────────┐    ┌─────────────────┐
│  Market         │     │  Financial      │    │  Strategic      │
│  Researcher     │───▶│  Analyst        │───▶│  Analyst        │
└─────────────────┘     └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Web Search     │     │  Financial      │     │  Strategic      │
│  Tools          │     │  Data APIs      │     │  Report         │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## ✨ Core Features

🤖 **Autonomous Planning & Decomposition**: Takes a high-level goal and breaks it down into executable sub-tasks.

🤝 **Multi-Agent Collaboration**: Specialized agents collaborate, passing data and refining work to solve complex problems.

🛠️ **Dynamic Tool Use**: Agents intelligently select and use the right tool for the job (e.g., web search for news, financial data APIs).

📊 **Structured Output**: The system culminates in a structured, professional report, not just a simple text response.

## 🎯 Agent Roles

- **Market Researcher**: Conducts comprehensive market analysis, competitor research, and industry trend identification
- **Financial Analyst**: Performs financial data analysis, ratio calculations, and investment recommendations
- **Strategic Analyst**: Synthesizes research into actionable business strategies and recommendations

## 🛠️ Tech Stack & Architecture

This project is built with a modern, open-source-first stack, designed for scalability and relevance in the current AI landscape.

**🤖 Agentic Framework**: CrewAI - Chosen for its clear, role-based structure that maps perfectly to our agent team concept.

**🧠 LLMs**: Groq with Llama4/DeepSeek & Gemini models - Inference on powerful open-source models with generous free tier.

**⚡ Backend**: FastAPI - High-performance Python framework for building our API endpoint.

**🎨 Frontend**: Streamlit - Beautiful, data-centric web app built purely in Python.

**🔧 Tooling & APIs**:

- **Web Search**: Tavily AI API - Search API optimized for AI agents
- **Financial Data**: Alpha Vantage API - Comprehensive financial and stock market data
- **Package Management**: UV - Next-generation Python package manager

**🚀 Deployment**:

- **Containerization**: Docker - Consistent deployment across environments
- **Hosting**: Streamlit Community Cloud / Hugging Face Spaces

## 🚀 Project Structure

```
StratAGI/
├── app/
│   ├── agents/              # CrewAI Agent definitions
│   │   ├── __init__.py
│   │   ├── financial_analyst.py
│   │   ├── market_researcher.py
│   │   └── strategist.py
│   ├── tasks/               # CrewAI Task definitions
│   │   ├── __init__.py
│   │   ├── financial_tasks.py
│   │   ├── market_tasks.py
│   │   └── report_tasks.py
│   ├── tools/               # Custom tool definitions
│   │   ├── __init__.py
│   │   ├── browser_tools.py
│   │   └── financial_tools.py
│   ├── main.py              # FastAPI application
│   └── crew.py              # Crew definition and assembly
├── frontend/
│   └── app.py               # Streamlit frontend application
├── .env.example             # Example environment variables
├── .gitignore               # Git ignore rules
├── Dockerfile               # Dockerfile for deployment
├── main.py                  # Main application entry point
├── pyproject.toml           # Project configuration and dependencies
├── README.md                # This file
├── requirements.txt         # Python dependencies (pip format)
├── start.sh                 # Application startup script
└── uv.lock                  # UV lock file for reproducible builds
```

## ⚙️ Setup and Installation

### Prerequisites

- **Python 3.12+** (recommended for optimal performance)
- **Git** for version control

### API Keys Required

You'll need API keys from:

- [Groq](https://groq.com/) - For LLM inference
- [Gemini](https://console.cloud.google.com/apis/credentials) - For Google Gemini LLM
- [Tavily AI](https://tavily.com/) - For web search capabilities
- [Alpha Vantage](https://www.alphavantage.co/) - For financial data

### Installation Steps

1. **Clone the repository:**

```bash
git clone https://github.com/shailesh-singh-ss/StratAGI.git
cd StratAGI
```

2. **Choose your installation method:**

**Option A: Using UV (Recommended)**

```bash
# Install UV if you haven't already
pip install uv

# Install dependencies with UV
uv sync
```

**Option B: Using pip with virtual environment**

```bash
# Create and activate virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

3. **Set up environment variables:**

```bash
# Copy the example environment file
cp .env.example .env
```

4. **Edit the `.env` file with your API keys:**

```env
GROQ_API_KEY="gsk_your_groq_api_key_here"
TAVILY_API_KEY="tvly-your_tavily_api_key_here"
ALPHA_VANTAGE_API_KEY="your_alpha_vantage_api_key_here"
ALPHA_VANTAGE_URL="https://www.alphavantage.co/query"
GEMINI_API_KEY="your_gemini_api_key_here"
```

## 🚀 Running the Application

### Quick Start (using the startup script)

```bash
# Make the script executable (Linux/Mac)
chmod +x start.sh

# Run the application
./start.sh
```

### Manual Start

1. **Start the FastAPI backend:**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

2. **In a new terminal, start the Streamlit frontend:**

```bash
streamlit run frontend/app.py
```

3. **Open your browser** to `http://localhost:8501` to use the application.

### Using Docker

```bash
# Build the Docker image
docker build -t stratagi .

# Run the container
docker run -p 8501:8501 -p 8000:8000 --env-file .env stratagi
```

## 🔧 Development

The project uses modern Python tooling for development:

| Tool               | Purpose                      |
| ------------------ | ---------------------------- |
| **UV**             | Fast dependency management   |
| **pyproject.toml** | Project configuration        |
| **CrewAI**         | Multi-agent orchestration    |
| **FastAPI**        | High-performance API backend |
| **Streamlit**      | Interactive frontend         |

## 🚀 Deployment

The application is containerized with Docker and can be deployed to:

- **Streamlit Community Cloud**
- **Hugging Face Spaces**
- **Any cloud provider** supporting Docker containers
- **Local infrastructure** with Docker

## 📝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

If you have any questions or need help, please:

- Open an [issue](https://github.com/shailesh-singh-ss/StratAGI/issues)
- Check the [documentation](https://github.com/shailesh-singh-ss/StratAGI/wiki)
- Join our community discussions

---

**Made with ❤️ by [Shailesh Singh](https://github.com/shailesh-singh-ss)**
