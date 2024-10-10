from pathlib import Path
from typing import Dict, Tuple

import toml


def load_toml_config(file_name: str = ".github-echo-config.toml") -> Dict:
    """
    Load and parse a TOML config file from the user's home directory.
    """
    home_dir = Path.home()
    config_path = home_dir / file_name

    if not config_path.exists():
        return {}

    try:
        with open(config_path, "r") as config_file:
            return toml.load(config_file)
    except toml.TomlDecodeError as e:
        raise RuntimeError(f"Failed to load or parse the config file: {str(e)}")


def parse_github_url(github_repository_url: str) -> Tuple[str, str]:
    """
    Extract username and repository name from a GitHub URL.
    """
    url_split_arr = github_repository_url.split("/")

    if len(url_split_arr) < 5 or not url_split_arr[3] or not url_split_arr[4]:
        raise ValueError(
            "Invalid GitHub URL format. Ensure the URL is in the form 'https://github.com/{username}/{repository}'."
        )

    return url_split_arr[3], url_split_arr[4]


def json_to_markdown(data: Dict[str, list]) -> str:
    """
    Convert a JSON-like dict to a Markdown formatted string.
    """
    result = ""

    for category, insights in data.items():
        if insights:
            formatted_category = format_category_name(category)
            result += f"## {formatted_category}\n"

            for insight in insights:
                title = insight.get("title", "").strip()
                description = insight.get("description", "").strip()

                if title and description:
                    result += f" - **{title}**: {description}\n"

            result += "\n"

    return result


def format_category_name(name: str) -> str:
    """
    Format a category name with capitalized words.
    """
    words = name.split("_")
    return " ".join(word.capitalize() for word in words)
