#!/bin/bash

# This script is the entrypoint for the Docker container.
# It starts both the FastAPI backend and the Streamlit frontend.

# Exit immediately if a command exits with a non-zero status.
set -e

# Start the FastAPI backend server in the background.
# The server will run on port 8000 and be accessible from outside the container.
echo "Starting FastAPI backend server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Start the Streamlit frontend server in the foreground.
# This will be the main process for the container.
# We disable runOnSave for production and ensure it listens on all network interfaces.
echo "Starting Streamlit frontend server..."
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0 --server.runOnSave=false
