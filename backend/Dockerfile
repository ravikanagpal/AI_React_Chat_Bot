# Use the official Python 3.12 image with Alpine Linux 3.18 as the base image
# Alpine is chosen for its small size, making the resulting image lightweight
FROM python:3.12-alpine3.18

# Set the working directory inside the container to /app
# All subsequent commands will operate relative to this directory
WORKDIR /app

# Copy the requirements file to the working directory
# This is typically used to list the Python dependencies
COPY requirements.txt .

# Install Python dependencies listed in requirements.txt
# --no-cache-dir ensures no unnecessary files are cached, keeping the image size small
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the parent directory to the working directory in the container
# This includes application code and other necessary files for the app
COPY .. .

# Expose port 8000 to allow external access to services running on this port
# This maps to FastAPI's default port used by Uvicorn
EXPOSE 8000

# Default command to start the FastAPI application using Uvicorn
# - `main:app` specifies the main file and the FastAPI app instance
# - `--host 0.0.0.0` makes the app accessible externally (not just inside the container)
# - `--port 8000` specifies the port the application will run on
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]