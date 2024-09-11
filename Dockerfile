# Bullseye was used as it provides a more comprehensive set of system libraries and tools compared to Alpine 
FROM python:3.9.20-bullseye@sha256:5591e6eab92348180676f2c1567a402fda5a51d91bf94648afd51905591c857d

WORKDIR /app

# Poetry is installed globally using pip
RUN pip install poetry

# PYTHONDONTWRITEBYTECODE=1: Prevents Python from writing .pyc files (compiled bytecode) to disk
# PYTHONUNBUFFERED=1: Ensures that the output from stdout and stderr is not buffered, so you see real-time output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV GOOGLE_GEMINI_API_KEY='Your API Key'
ENV GITHUB_API_TOKEN='Your API Key'
ENV GITHUB_API_VERSION='2022-11-28'

# Copy the application code and configuration files into the container
COPY _main.py _config.py pyproject.toml poetry.lock* /app/
COPY application /app/application

# Configure Poetry to install dependencies directly into the system Python environment
# --no-root means Poetry will not install the current project itself (useful when you only need dependencies)
RUN poetry install --no-root

# This specifies the default command to run when the container starts
ENTRYPOINT ["poetry", "run", "python", "_main.py"]
