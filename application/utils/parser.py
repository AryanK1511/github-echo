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


def parse_json_string(markdown_string: str) -> dict[str,str]:
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


def json_to_markdown(data: dict):
    try:
        # Parse the JSON string

        # Start with an empty result string
        result = ""

        # Iterate through the top-level keys (main categories)
        for category, subcategories in data["GitHubInsights"].items():
            # Add the category as a header
            result += f"**{category.replace('_', ' ').title()}:**\n"

            # Iterate through the subcategories
            for item in subcategories:
                # Add each subcategory as a bullet point
                result += f" - {item['title']}: {item['description']}\n"
                result += "\n"

            # Add a newline for spacing between categories
            result += "\n"

        return result

    except json.JSONDecodeError:
        return "Error: Invalid JSON string"
    except KeyError:
        return "Error: JSON structure does not match expected format"
