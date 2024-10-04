# F.Khan Edited: 03-10-2024
from pathlib import Path
from typing import Dict

import toml


def load_toml_config(file_name: str = ".github-echo-config.toml") -> Dict:
    """
    Load and parse the TOML config file from the user's home directory.

    Args:
        file_name (str): The name of the configuration file.

    Returns:
        dict: A dictionary with the configuration options.
    """
    home_dir = Path.home()  # Get the user's home directory
    config_path = home_dir / file_name  # Construct the full path to the dotfile

    if not config_path.exists():
        # If the dotfile doesn't exist, return an empty dictionary
        return {}

    try:
        # Trying to open and parse the TOML file
        with open(config_path, "r") as config_file:
            return toml.load(config_file)
    except toml.TomlDecodeError as e:
        # If parsing the file fails, raise an error
        raise RuntimeError(f"Failed to load or parse the config file: {str(e)}")


def parse_github_url(github_repository_url: str) -> tuple[str, str]:
    """
    Parses a GitHub repository URL and extracts the username and repository name.

    Args:
        github_repository_url (str): The URL of the GitHub repository to parse.

    Returns:
        tuple: A tuple containing the username and repository name as (username, repository_name).
    """
    try:
        # Split the URL by "/" and extract username and repository name
        url_split_arr = github_repository_url.split("/")

        # Validate that the split array has at least 5 elements: https://github.com/{username}/{repository}
        if len(url_split_arr) < 5 or not url_split_arr[3] or not url_split_arr[4]:
            raise ValueError(
                "Invalid GitHub URL format. Ensure the URL is in the form 'https://github.com/{username}/{repository}'."
            )

        # Return the username and repository name
        return url_split_arr[3], url_split_arr[4]

    except IndexError:
        # Raise a more descriptive error in case of URL issues
        raise ValueError("Invalid GitHub URL provided.")


def json_to_markdown(data: str) -> str:
    """
    Convert a JSON-like dictionary to a Markdown formatted string.

    Args:
        data (str): A JSON string containing insights data, with categories mapping to lists of insights.

    Returns:
        str: A Markdown formatted string representing the input data. Each category is formatted as a header with bullet points for insights.
    """
    result = ""

    for category, insights in data.items():
        if insights:
            # Format the category name
            formatted_category = format_category_name(category)
            # Add the category as a header
            result += f"## {formatted_category}\n"

            for insight in insights:
                if isinstance(insight, dict):
                    title = insight.get("title", "").strip()
                    description = insight.get("description", "").strip()

                    # Add each insight as a bullet point only if both title and description are present
                    if title and description:
                        result += f" - **{title}**: {description}\n"

            # Add a newline for spacing between categories
            result += "\n"

    return result


def format_category_name(name: str) -> str:
    """
    Format a category name by splitting it into words and capitalizing each word.

    Args:
        name (str): The input string to be formatted.

    Returns:
        str: A formatted string with each word capitalized and separated by spaces.
    """
    words = name.split("_")
    return " ".join(word.capitalize() for word in words)
