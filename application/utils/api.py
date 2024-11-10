from typing import Any, Dict

import httpx

import _constants
from _config import GITHUB_API_TOKEN


async def query_github(url: str) -> Dict[str, Any]:
    """
    Makes an asynchronous GET request to the provided GitHub API URL and returns the JSON response.
    """

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {GITHUB_API_TOKEN}',
        'X-GitHub-Api-Version': _constants.GITHUB_API_VERSION,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
