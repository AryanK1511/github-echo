import re
import json


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


def parse_json_string(markdown_string: str) -> dict[str, str]:
    """
    Converts markdown string containing JSON code block to a JSON string.
    Strips markdown code block indicators and language specifier(this is returned by gemini model as response)

    Args: markdown_string (str): The markdown string containing JSON code block.

    Returns: str | None: The JSON string if successfully parsed, otherwise None.
    """
    # Remove the markdown code block indicators and language specifier
    json_string = re.sub(r"```json\s*\n", "", markdown_string)
    json_string = re.sub(r"\n```\s*$", "", json_string)

    try:
        # Load the JSON string
        data: dict[str, str] = json.loads(json_string)
        return data
        # return json_string

    except json.JSONDecodeError:
        raise ValueError("Error encoding generated string.")


def json_to_markdown(data: dict) -> str:
    """
    Convert a JSON-like dictionary to a Markdown formatted string.

    This function takes a dictionary containing GitHub insights data and converts it
    into a Markdown formatted string. It can handle different input structures and
    formatting styles for category names.

    Args:
        data (dict): A dictionary containing GitHub insights data. It can be in two formats:
            1. {"GitHubInsights": {...}} where the inner dictionary contains the actual data.
            2. {...} where the dictionary directly contains the data.

    Returns:
        str: A Markdown formatted string representing the input data. Each main category
             is formatted as a header, with subcategories as bullet points.

    Raises:
        Exception: If any error occurs during processing, it's caught, printed,
                   and an empty string is returned.

    Example:
        >>> data = {
        ...     "summary": {
        ...         "total_repos": "10 repositories",
        ...         "total_stars": "100 stars"
        ...     }
        ... }
        >>> print(json_to_markdown(data))
        **Summary:**
         - Total Repos: 10 repositories
         - Total Stars: 100 stars

    """
    try:
        # Start with an empty result string
        result = ""
        # Check if "GitHubInsights" is in the data(as specified in the schema), if not use the data directly
        insights = data.get("GitHubInsights", data)
        # Iterate through the top-level keys (main categories)
        for category, subcategories in insights.items():
            # Format the category name
            formatted_category = format_category_name(category)
            # Add the category as a header
            result += f"**{formatted_category}:**\n"
            # Check if subcategories is a list of dictionaries or a single dictionary
            if isinstance(subcategories, list):
                for item in subcategories:
                    # Add each subcategory as a bullet point
                    result += f" - {item['title']}: {item['description']}\n"
            elif isinstance(subcategories, dict):
                for title, description in subcategories.items():
                    # Add each key-value pair as a bullet point
                    result += f" - {format_category_name(title)}: {description}\n"
            # Add a newline for spacing between categories
            result += "\n"
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


def format_category_name(name: str) -> str:
    """
    Format a category name by splitting it into words and capitalizing each word.

    This function takes a string that may be in camelCase, snake_case, or kebab-case,
    splits it into individual words, capitalizes each word, and joins them with spaces.

    Args:
        name (str): The input string to be formatted.

    Returns:
        str: A formatted string with each word capitalized and separated by spaces.

    Example:
        >>> format_category_name("repo_summary")
        'Repo Summary'
        >>> format_category_name("totalStars")
        'Total Stars'
        >>> format_category_name("pull-requests")
        'Pull Requests'
    """
    # Split the string by underscores, hyphens, or capital letters
    words = re.findall(r"[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+", name)
    # Capitalize each word and join them with spaces
    return " ".join(word.capitalize() for word in words)
