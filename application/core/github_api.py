import asyncio
from typing import Any, Dict

from application.utils.api import query_github


# Main function to fetch all data concurrently
async def fetch_github_data(owner: str, repo: str) -> Dict[str, Any]:
    """
    Fetches and combines various data points about a GitHub repository using the GitHub API.

    This asynchronous function gathers information about a specified GitHub repository by
    making concurrent requests to various GitHub API endpoints, including metadata, commit history,
    contributors, issues, pull requests, releases, languages, and community profile.

    Args:
        owner (str): The GitHub username or organization name that owns the repository.
        repo (str): The name of the repository to fetch data for.

    Returns:
        Dict[str, Any]: A dictionary containing combined data from multiple GitHub API calls, organized
                        into sections such as repository metadata, commit history, contributors, issues,
                        pull requests, releases, languages, and community profile.

    Example:
    """

    # Run all the fetch functions concurrently

    results = await asyncio.gather(
        fetch_repo_metadata(owner, repo),
        fetch_commits_history(owner, repo),
        fetch_contributors(owner, repo),
        fetch_issues(owner, repo),
        fetch_pull_requests(owner, repo),
        fetch_releases(owner, repo),
        fetch_languages(owner, repo),
        fetch_community_profile(owner, repo),
    )

    # Raise an error if any of the fetch functions failed or no data was returned
    if any(result is None for result in results):
        raise ValueError("Failed to fetch data for the repository")

    # Combine the results into a single JSON object and return it
    combined_data = {
        "repository_metadata": results[0],
        "commit_history": results[1],
        "contributors": results[2],
        "issues": results[3],
        "pull_requests": results[4],
        "releases": results[5],
        "languages": results[6],
        "community_profile": results[7],
    }

    return combined_data


# Function to fetch repository metadata
async def fetch_repo_metadata(owner: str, repo: str) -> Dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    metadata = await query_github(url)

    relevant_fields = [
        "name",
        "full_name",
        "description",
        "html_url",
        "homepage",
        "license",
        "stargazers_count",
        "watchers_count",
        "forks_count",
        "open_issues_count",
        "subscribers_count",
        "created_at",
        "updated_at",
        "pushed_at",
        "size",
        "language",
        "topics",
    ]

    return {field: metadata.get(field, None) for field in relevant_fields}


# Function to fetch commits history
async def fetch_commits_history(owner: str, repo: str) -> Dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    commits = await query_github(url)

    relevant_fields = ["sha", "author", "committer", "message", "url"]

    return [
        {
            field: (
                commit.get("commit", {}).get(field, None)
                if field in ["author", "committer"]
                else commit.get(field, None)
            )
            for field in relevant_fields
        }
        for commit in commits
    ]


# Function to fetch contributors
async def fetch_contributors(owner: str, repo: str) -> Dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    contributors = await query_github(url)

    relevant_fields = ["login", "id", "avatar_url", "html_url", "contributions"]

    return [
        {field: contributor.get(field, None) for field in relevant_fields}
        for contributor in contributors
    ]


# Function to fetch issues
async def fetch_issues(owner: str, repo: str) -> Dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    return await query_github(url)


# Function to fetch pull requests
async def fetch_pull_requests(owner: str, repo: str) -> Dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

    return await query_github(url)


# Function to fetch releases
async def fetch_releases(owner: str, repo: str) -> Dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"

    # Return data for all releases
    return await query_github(url)


# Function to fetch languages used in the repository
async def fetch_languages(owner: str, repo: str) -> Dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"

    # Return the complete language data
    return await query_github(url)


# Function to fetch community profile
async def fetch_community_profile(owner: str, repo: str) -> Dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo}/community/profile"

    # Return the complete community profile
    return await query_github(url)
