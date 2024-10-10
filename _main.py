#!/usr/bin/env python3

import asyncio
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from typing_extensions import Annotated

from application.utils.callbacks import (
    handle_error,
    load_config_values,
    process_repository_tasks,
    version_callback,
)
from application.utils.parser import load_toml_config

# Console instances for standard and error output
console = Console(soft_wrap=True)
err_console = Console(stderr=True, soft_wrap=True)

# Initialize the Typer app
app = typer.Typer(
    no_args_is_help=True,
    help="CLI tool built to obtain in-depth, actionable information about GitHub repositories.",
)


@app.callback(invoke_without_command=True)
def github_repo_insights(
    github_repository_url: Annotated[
        Optional[str],
        typer.Argument(..., help="The URL of the GitHub repository to analyze"),
    ],
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            help="Get the version number",
            is_eager=True,
            callback=version_callback,
        ),
    ] = None,
    model: Annotated[
        Optional[str],
        typer.Option(
            "--model",
            "-m",
            help="Choose the LLM that you want to be used to generate insights. Can be 'gemini' or 'groq'.",
        ),
    ] = "gemini",
    model_temperature: Annotated[
        Optional[float],
        typer.Option(
            "--temperature",
            "-t",
            help="Sets the temperature for the model, with a range from 0.0 (more deterministic) to 2.0 (more random).",
        ),
    ] = 0.5,
    output_file: Annotated[
        Optional[Path], typer.Option("--output", "-o", help="Path to the output file")
    ] = None,
    token_usage: Annotated[
        bool, typer.Option("--token-usage", help="Flag for printing token usage")
    ] = False,
):
    """
    Main function to analyze a GitHub repository and optionally output the results to a file.

    Args:
        github_repository_url (str): Required. The URL of the GitHub repository to analyze.
        version (Optional[bool]): Optional. If provided, prints the version number and exits the application.
        output_file (Optional[Path]): Optional. If provided, the path to a file where the Markdown summary will be saved.
    """

    # Load the TOML config from home directory
    config = load_toml_config(".github-echo-config.toml")
    if not config:
        err_console.print(
            ":warning: [bold yellow]Warning:[/] configuration file not found. Using default values.",
            style="bold yellow",
        )

    # Load configuration values
    model, model_temperature, output_file, token_usage = load_config_values(config)

    try:
        asyncio.run(
            process_repository_tasks(
                repo_url=github_repository_url,
                selected_model=model,
                temperature_setting=model_temperature,
                output_file=output_file,
                token_usage=token_usage,
            )
        )
    except Exception as e:
        handle_error(e)


# Run the app
if __name__ == "__main__":
    app()
