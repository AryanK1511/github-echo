import re
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

err_console = Console(stderr=True)


def check_cli_arguments(
    github_repository_url: str,
    model: Optional[str],
    model_temperature: Optional[float],
    output_file: Optional[Path],
) -> None:
    """
    Validates the command-line arguments for a GitHub repository analysis tool,
    including checking if the required API keys for the selected model are present.
    """
    # Validate GitHub repository URL
    github_api_url_pattern = (
        r'^https://(www\.)?github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?$'
    )
    if not re.match(github_api_url_pattern, github_repository_url):
        raise typer.BadParameter(
            'Invalid GitHub repository URL. Please provide a valid URL in the '
            'format: https://github.com/username/repository or similar formats '
            'allowed by GitHub.'
        )

    if not model:
        raise typer.BadParameter(
            'Model must be specified either in CLI or config. '
            'Please choose either "gemini" or "groq".'
        )

    if model and model not in ['gemini', 'groq']:
        raise typer.BadParameter(
            'Invalid model. Please choose either "gemini" or "groq".'
        )

    if not model_temperature:
        raise typer.BadParameter(
            'Model temperature must be specified either in CLI or config.'
        )

    if model_temperature is not None and not (0 <= model_temperature <= 1):
        raise typer.BadParameter(
            'Invalid model temperature. The value should be between 0 and 1.'
        )

    if output_file:
        if output_file.is_dir():
            raise typer.BadParameter(
                'Invalid output file. The path points to a directory, but a file '
                'path is expected.'
            )
        if not output_file.parent.exists():
            raise typer.BadParameter(
                'Invalid output file path. The directory of the specified file does '
                'not exist.'
            )
