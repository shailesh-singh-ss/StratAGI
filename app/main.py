import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file at the start
load_dotenv()

# Import our crew class
from app.crew import StratAGICrew

# --- FastAPI App Initialization ---
app = FastAPI(
    title="StratAGI API",
    description="An API for running the StratAGI multi-agent business analysis crew.",
    version="1.0.0"
)

# --- Pydantic Model for Request Body ---
# This model defines the expected structure and data types for incoming API requests.
class AnalysisRequest(BaseModel):
    company: str
    market: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "company": "NVIDIA",
                "market": "AI Hardware"
            }
        }

# --- API Endpoints ---

@app.get("/", tags=["Status"])
def read_root():
    """
    Root endpoint to check if the API is running.
    """
    return {"status": "StratAGI API is running successfully."}


@app.post("/analyze", tags=["Analysis"])
async def analyze_company(request: AnalysisRequest):
    """
    The main endpoint to trigger the business analysis.
    It accepts a company and a market, runs the agent crew, and returns the final report.
    """
    # Check for necessary API keys before starting
    required_keys = ["GROQ_API_KEY", "TAVILY_API_KEY", "ALPHA_VANTAGE_API_KEY"]
    if not all(os.getenv(key) for key in required_keys):
        raise HTTPException(
            status_code=500, 
            detail="One or more required API keys (GROQ, TAVILY, ALPHA_VANTAGE) are missing from the environment."
        )

    try:
        # Create an instance of the crew with the provided data
        stratagi_crew = StratAGICrew(request.company, request.market)
        
        # Run the crew's analysis process
        result = stratagi_crew.run()
        
        # Return the final report
        return {"report": result}

    except Exception as e:
        # Catch any exceptions during the crew's execution and return a detailed error
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred during the analysis process: {str(e)}"
        )

