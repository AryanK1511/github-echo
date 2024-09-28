import os
import re
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

# Initialize console for error messages
err_console = Console(stderr=True)


def check_cli_arguments(
    github_repository_url: str,
    model: Optional[str],
    model_temperature: Optional[float],
    output_file: Optional[Path],
) -> None:
    """
    Validates the command-line arguments for a GitHub repository analysis tool, including checking
    if the required API keys for the selected model are present.

    Args:
        github_repository_url (str): The URL or SSH path of the GitHub repository to analyze.
                                     It should be a valid GitHub URL accepted by the GitHub API.
        model (Optional[str]): The model to use for analysis. Can be either 'gemini' or 'groq'. If no model is provided,
                               this is ignored.
        model_temperature (Optional[float]): A temperature value for the model's behavior. Must be between 0 and 1 if provided.
        output_file (Optional[Path]): The path to an output file where results will be saved. Must be a valid file path and
                                      not a directory if provided.

    Raises:
        typer.BadParameter: If any of the inputs are invalid. Provides detailed error messages explaining
                            what is wrong and how to fix it.
    """
    # Validate GitHub repository URL
    github_api_url_pattern = (
        r"^https://(www\.)?github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?$"
    )
    if not re.match(github_api_url_pattern, github_repository_url):
        raise typer.BadParameter(
            "Invalid GitHub repository URL. Please provide a valid URL in the format: "
            "https://github.com/username/repository or similar formats allowed by GitHub."
        )

    # Validate model
    if model and model not in ["gemini", "groq"]:
        raise typer.BadParameter(
            'Invalid model. Please choose either "gemini" or "groq".'
        )

    # Check for required API key based on the model
    if model == "gemini":
        if not os.getenv("GOOGLE_GEMINI_API_KEY"):
            raise typer.BadParameter(
                "GOOGLE_GEMINI_API_KEY is required for the gemini model but not found in the environment."
            )
    elif model == "groq":
        if not os.getenv("GROQ_API_KEY"):
            raise typer.BadParameter(
                "GROQ_API_KEY is required for the groq model but not found in the environment."
            )

    # Validate model_temperature
    if model_temperature is not None and not (0 <= model_temperature <= 1):
        raise typer.BadParameter(
            "Invalid model temperature. The value should be between 0 and 1."
        )

    # Validate output file
    if output_file:
        if output_file.is_dir():
            raise typer.BadParameter(
                "Invalid output file. The path points to a directory, but a file path is expected."
            )
        if not output_file.parent.exists():
            raise typer.BadParameter(
                "Invalid output file path. The directory of the specified file does not exist."
            )
