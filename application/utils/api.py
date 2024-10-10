from typing import Any, Dict

import httpx

from _config import GITHUB_API_TOKEN, GITHUB_API_VERSION


async def query_github(url: str) -> Dict[str, Any]:
    """
    Makes an asynchronous GET request to the provided GitHub API URL and returns the JSON response.
    """

    # Define the headers to be included in the request
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_API_TOKEN}",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
