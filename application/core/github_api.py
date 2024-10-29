import asyncio
from typing import Any, Dict

import httpx
import typer

from application.utils.api import query_github


# Main function to fetch all data concurrently
async def fetch_github_data(owner: str, repo: str) -> Dict[str, Any]:
    """
    Fetches and combines various data points about a GitHub repository using the GitHub API.
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

    # Combine the results into a single JSON object and return it
    combined_data = {
        'repository_metadata': results[0],
        'commit_history': results[1],
        'contributors': results[2],
        'issues': results[3],
        'pull_requests': results[4],
        'releases': results[5],
        'languages': results[6],
        'community_profile': results[7],
    }

    return combined_data


# Function to fetch repository metadata
async def fetch_repo_metadata(owner: str, repo: str) -> Dict[str, Any]:
    url = f'https://api.github.com/repos/{owner}/{repo}'
    try:
        metadata = await query_github(url)
        relevant_fields = [
            'name',
            'full_name',
            'description',
            'html_url',
            'homepage',
            'license',
            'stargazers_count',
            'watchers_count',
            'forks_count',
            'open_issues_count',
            'subscribers_count',
            'created_at',
            'updated_at',
            'pushed_at',
            'size',
            'language',
            'topics',
        ]
        return {field: metadata.get(field, None) for field in relevant_fields}

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            raise typer.Exit('Unauthorized: Check your GitHub API Key.') from e
        elif e.response.status_code == 404:
            raise typer.Exit(f"Repository '{owner}/{repo}' not found.") from e
        else:
            raise typer.Exit(
                f'Error fetching metadata: {e.response.status_code} - {e.response.text}'
            ) from e

    except Exception as e:
        raise typer.Exit(
            f"Failed to fetch metadata for repository '{owner}/{repo}': {e}"
        ) from e


# Function to fetch commits history
async def fetch_commits_history(owner: str, repo: str) -> Dict[str, Any]:
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    try:
        commits = await query_github(url)
        relevant_fields = ['sha', 'author', 'committer', 'message', 'url']

        return [
            {
                field: (
                    commit.get('commit', {}).get(field, None)
                    if field in ['author', 'committer']
                    else commit.get(field, None)
                )
                for field in relevant_fields
            }
            for commit in commits
        ]

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            raise typer.Exit('Unauthorized: Check your GitHub API Key.') from e
        elif e.response.status_code == 404:
            raise typer.Exit(
                f"Commits not found for repository '{owner}/{repo}'."
            ) from e
        else:
            raise typer.Exit(
                f'Error fetching commit history: {e.response.status_code} - {e.response.text}'
            ) from e

    except Exception as e:
        raise typer.Exit(
            f"Failed to fetch commit history for repository '{owner}/{repo}': {e}"
        ) from e


# Function to fetch contributors
async def fetch_contributors(owner: str, repo: str) -> Dict[str, Any]:
    url = f'https://api.github.com/repos/{owner}/{repo}/contributors'
    try:
        contributors = await query_github(url)
        relevant_fields = [
            'login',
            'id',
            'avatar_url',
            'html_url',
            'contributions',
        ]

        return [
            {field: contributor.get(field, None) for field in relevant_fields}
            for contributor in contributors
        ]

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            raise typer.Exit('Unauthorized: Check your GitHub API Key.') from e
        elif e.response.status_code == 404:
            raise typer.Exit(
                f"Contributors not found for repository '{owner}/{repo}'."
            ) from e
        else:
            raise typer.Exit(
                f'Error fetching contributors: {e.response.status_code} - {e.response.text}'
            ) from e

    except Exception as e:
        raise typer.Exit(
            f"Failed to fetch contributors for repository '{owner}/{repo}': {e}"
        ) from e


# Function to fetch issues
async def fetch_issues(owner: str, repo: str) -> Dict[str, Any]:
    url = f'https://api.github.com/repos/{owner}/{repo}/issues'
    try:
        issues = await query_github(url)
        return issues

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            raise typer.Exit('Unauthorized: Check your GitHub API Key.') from e
        elif e.response.status_code == 404:
            raise typer.Exit(
                f"Issues not found for repository '{owner}/{repo}'."
            ) from e
        else:
            raise typer.Exit(
                f'Error fetching issues: {e.response.status_code} - {e.response.text}'
            ) from e

    except Exception as e:
        raise typer.Exit(
            f"Failed to fetch issues for repository '{owner}/{repo}': {e}"
        ) from e


# Function to fetch pull requests
async def fetch_pull_requests(owner: str, repo: str) -> Dict[str, Any]:
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    try:
        pulls = await query_github(url)
        return pulls

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            raise typer.Exit('Unauthorized: Check your GitHub API Key.') from e
        elif e.response.status_code == 404:
            raise typer.Exit(
                f"Pull requests not found for repository '{owner}/{repo}'."
            ) from e
        else:
            raise typer.Exit(
                f'Error fetching pull requests: {e.response.status_code} - {e.response.text}'
            ) from e

    except Exception as e:
        raise typer.Exit(
            f"Failed to fetch pull requests for repository '{owner}/{repo}': {e}"
        ) from e


# Function to fetch releases
async def fetch_releases(owner: str, repo: str) -> Dict[str, Any]:
    url = f'https://api.github.com/repos/{owner}/{repo}/releases'
    try:
        releases = await query_github(url)
        return releases

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            raise typer.Exit('Unauthorized: Check your GitHub API Key.') from e
        elif e.response.status_code == 404:
            raise typer.Exit(
                f"Releases not found for repository '{owner}/{repo}'."
            ) from e
        else:
            raise typer.Exit(
                f'Error fetching releases: {e.response.status_code} - {e.response.text}'
            ) from e

    except Exception as e:
        raise typer.Exit(
            f"Failed to fetch releases for repository '{owner}/{repo}': {e}"
        ) from e


# Function to fetch languages used in the repository
async def fetch_languages(owner: str, repo: str) -> Dict[str, Any]:
    url = f'https://api.github.com/repos/{owner}/{repo}/languages'
    try:
        languages = await query_github(url)
        return languages

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            raise typer.Exit('Unauthorized: Check your GitHub API Key.') from e
        elif e.response.status_code == 404:
            raise typer.Exit(
                f"Languages not found for repository '{owner}/{repo}'."
            ) from e
        else:
            raise typer.Exit(
                f'Error fetching languages: {e.response.status_code} - {e.response.text}'
            ) from e

    except Exception as e:
        raise typer.Exit(
            f"Failed to fetch languages for repository '{owner}/{repo}': {e}"
        ) from e


# Function to fetch community profile information
async def fetch_community_profile(owner: str, repo: str) -> Dict[str, Any]:
    url = f'https://api.github.com/repos/{owner}/{repo}/community/profile'
    try:
        community_profile = await query_github(url)
        relevant_fields = [
            'health_percentage',
            'description',
            'files',
            'notes',
            'status',
            'files',
            'activity',
        ]
        return {
            field: community_profile.get(field, None)
            for field in relevant_fields
        }

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            raise typer.Exit('Unauthorized: Check your GitHub API Key.') from e
        elif e.response.status_code == 404:
            raise typer.Exit(
                f"Community profile not found for repository '{owner}/{repo}'."
            ) from e
        else:
            raise typer.Exit(
                f'Error fetching community profile: {e.response.status_code} - {e.response.text}'
            ) from e

    except Exception as e:
        raise typer.Exit(
            f"Failed to fetch community profile for repository '{owner}/{repo}': {e}"
        ) from e
