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
