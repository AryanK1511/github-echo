import os
from os.path import abspath, dirname, join

from dotenv import load_dotenv
from rich.console import Console

# Console instances for standard and error output
err_console = Console(stderr=True, soft_wrap=True)


dotenv_path = join(dirname(abspath(__file__)), '.env')

# Check if the .env file exists before trying to load it
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Load environment variables
GOOGLE_GEMINI_API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GITHUB_API_TOKEN = os.getenv('GITHUB_API_TOKEN')
GITHUB_API_VERSION = os.getenv('GITHUB_API_VERSION')

# Print a warning if required environment variables are missing
if not GITHUB_API_TOKEN:
    err_console.print(
        ':warning: [bold yellow]Warning:[/] GITHUB_API_TOKEN not found.',
        style='bold yellow',
    )

if not GITHUB_API_VERSION:
    err_console.print(
        ':warning: [bold yellow]Warning:[/] GITHUB_API_VERSION not found.',
        style='bold yellow',
    )
