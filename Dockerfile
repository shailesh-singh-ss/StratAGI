# --- Base Stage ---
# Use an official Python runtime as a parent image.
# The 'slim' variant is a good choice for production as it's smaller.
FROM python:3.10-slim

# --- Metadata ---
LABEL author="Shailesh Singh"
LABEL project="StratAGI"

# --- Environment Variables ---
# Set the working directory in the container
WORKDIR /app

# Prevents Python from writing pyc files to disc (improves performance in containers)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (makes logs appear in real-time)
ENV PYTHONUNBUFFERED 1

# --- System Dependencies ---
# Update package lists and install necessary build tools and git.
# Clean up apt-get cache to keep the image size small.
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# --- Python Dependencies ---
# Copy the requirements file first to leverage Docker's layer caching.
# If requirements.txt doesn't change, this layer won't be re-built.
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# --- Application Code ---
# Copy the rest of the application source code into the container
COPY . .

# --- Permissions ---
# Make the startup script executable
RUN chmod +x ./start.sh

# --- Expose Ports ---
# Expose the port for the FastAPI backend
EXPOSE 8000
# Expose the port for the Streamlit frontend
EXPOSE 8501

# --- Entrypoint ---
# Run the startup script when the container launches
CMD ["./start.sh"]
