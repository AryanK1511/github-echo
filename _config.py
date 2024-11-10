import os
import sys
from os.path import abspath, dirname, join

import typer
from dotenv import load_dotenv
from rich.console import Console

import _constants
from application.utils.parser import load_toml_config

err_console = Console(stderr=True, soft_wrap=True)


config = load_toml_config(_constants.CONFIG_FILE)

dotenv_path = join(dirname(abspath(__file__)), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

GOOGLE_GEMINI_API_KEY = config.get('api_keys', {}).get(
    'google_gemini_api_key'
) or os.getenv('google_gemini_api_key')

GROQ_API_KEY = config.get('api_keys', {}).get('groq_api_key') or os.getenv(
    'groq_api_key'
)

GITHUB_API_TOKEN = config.get('api_keys', {}).get(
    'github_api_token'
) or os.getenv('github_api_token')

if not GITHUB_API_TOKEN:
    err_console.print(
        '\n[red]🚨 [bold]Error:[/bold] github_api_token not found 🚨\n'
    )
    typer.Exit(code=1)
    sys.exit(1)

if not GOOGLE_GEMINI_API_KEY:
    err_console.print(
        ':warning: [bold yellow]Warning:[/] google_gemini_api_key not found. You will not be',
        'able to use the gemini model without this',
        style='bold yellow',
    )

if not GROQ_API_KEY:
    err_console.print(
        ':warning: [bold yellow]Warning:[/] groq_api_key not found. You will not be able'
        ' to use the groq model without this',
        style='bold yellow',
    )
