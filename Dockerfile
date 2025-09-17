# ========== Builder Stage ==========
FROM python:3.11.6-slim-bookworm as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set work directory
WORKDIR /app

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock* ./

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install itsdangerous==2.1.2 starlette==0.27.0 fastapi==0.104.1 uvicorn==0.24.0 python-dotenv==1.0.0 pydantic==1.10.13 jinja2==3.1.2 python-multipart==0.0.6

# ========== Production Stage ==========
FROM python:3.11.6-slim-bookworm as production

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install required system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies directly in the production stage
RUN pip install --upgrade pip && \
    pip install itsdangerous==2.1.2 starlette==0.27.0 fastapi==0.104.1 uvicorn==0.24.0 python-dotenv==1.0.0 pydantic==1.10.13 jinja2==3.1.2 python-multipart==0.0.6

# Create a non-root user
RUN addgroup --system appuser && adduser --system --no-create-home --group appuser

# Create static directory and set permissions
RUN mkdir -p /app/static && \
    chown -R appuser:appuser /app/static

# Copy application code
COPY . .

# Set file permissions
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose the port where FastAPI will run
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Command to start the app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
