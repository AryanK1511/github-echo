import os
from os.path import abspath, dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(abspath(__file__)), ".env")
load_dotenv(dotenv_path)

# Load all environment variables
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
GITHUB_API_VERSION = os.getenv("GITHUB_API_VERSION")
