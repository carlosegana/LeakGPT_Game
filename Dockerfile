# Use an official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements files and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port where FastAPI will run
EXPOSE 8000

# Command to start the app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]