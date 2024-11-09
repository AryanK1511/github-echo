from pathlib import Path
from typing import Dict, Tuple

import toml


def load_toml_config(file_name: str) -> Dict:
    """
    Load and parse a TOML config file from the user's home directory.
    """
    home_dir = Path.home()
    config_path = home_dir / file_name

    if not config_path.exists():
        return {}

    try:
        with open(config_path) as config_file:
            return toml.load(config_file)
    except toml.TomlDecodeError as e:
        raise RuntimeError(
            f'Failed to load or parse the config file: {str(e)}'
        ) from e


def parse_github_url(github_repository_url: str) -> Tuple[str, str]:
    """
    Extract username and repository name from a GitHub URL.
    """
    url_split_arr = github_repository_url.split('/')

    if len(url_split_arr) < 5 or not url_split_arr[3] or not url_split_arr[4]:
        raise ValueError(
            "Invalid GitHub URL format. Ensure the URL is in the form 'https://github.com/{username}/{repository}'."
        )

    return url_split_arr[3], url_split_arr[4]


def json_to_markdown(data: Dict[str, list]) -> str:
    """
    Convert a JSON-like dict to a Markdown formatted string.
    """
    result = ''

    for category, insights in data.items():
        # Filter out insights that don't have both a title and description
        valid_insights = [
            insight
            for insight in insights
            if insight.get('title', '').strip()
            and insight.get('description', '').strip()
        ]

        # If no valid insights exist for the category, skip it
        if not valid_insights:
            continue

        # Format category name and add to result
        formatted_category = format_category_name(category)
        result += f'## {formatted_category}\n'

        # Add valid insights to the category
        for insight in valid_insights:
            title = insight['title'].strip()
            description = insight['description'].strip()
            result += f' - **{title}**: {description}\n'

        result += '\n'

    return result


def format_category_name(name: str) -> str:
    """
    Format a category name with capitalized words.
    """
    words = name.split('_')
    return ' '.join(word.capitalize() for word in words)
