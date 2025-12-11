# Use a Python image with uv pre-installed
# Stage 1: Builder - Installs dependencies
FROM python:3.12-slim

# Install the project into `/app`
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

EXPOSE 8000

# Define the command to run the application when the container starts
CMD ["python","-m","uvicorn","agent:a2a_app","--host","0.0.0.0","--port","8000"]
