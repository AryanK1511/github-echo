import os
from os.path import abspath, dirname, join

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
