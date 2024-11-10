#!/usr/bin/env python3
import asyncio
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

import _constants
from application.utils.helpers import (
    get_cli_version,
    handle_error,
    process_repository_tasks,
)
from application.utils.parser import load_toml_config

console = Console(soft_wrap=True)
err_console = Console(stderr=True, soft_wrap=True)


app = typer.Typer(
    no_args_is_help=True,
    help='CLI tool built to obtain in-depth, actionable information about '
    'GitHub repositories.',
)


@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(
        None,
        '--version',
        '-v',
        help='Show the version of the application',
        is_eager=True,
    ),
):
    """
    Main function that will run for any subcommand, handles the version option.
    """
    if version:
        get_cli_version(version)


@app.command(
    name='analyze',
    help='Analyze a GitHub repository and optionally output the results to a file.',
)
def analyze(
    github_repository_url: str = typer.Argument(
        ..., help='The URL of the GitHub repository to analyze'
    ),
    model: Optional[str] = typer.Option(
        None,
        '--model',
        '-m',
        help="Choose the LLM to generate insights, e.g., 'gemini' or 'groq'.",
    ),
    model_temperature: Optional[float] = typer.Option(
        None,
        '--model-temperature',
        '-t',
        help='Sets the temperature for the model, ranging from '
        '0.0 (deterministic) to 2.0 (random).',
    ),
    token_usage: Optional[bool] = typer.Option(
        None, '--show-token-usage', help='Flag for printing token usage'
    ),
    output_file: Optional[Path] = typer.Option(
        None,
        '--output-file',
        '-o',
        help='Choose which file to show the response in (could be a relative or absolute path)',
    ),
):
    config = load_toml_config(_constants.CONFIG_FILE) or {}
    if not config:
        err_console.print(
            '\n:warning: [bold yellow]Warning:[/] configuration file not found. ',
            style='bold yellow',
        )

    selected_model = (
        model if model is not None else config.get('settings', {}).get('model')
    )

    temperature_setting = (
        model_temperature
        if model_temperature is not None
        else config.get('settings', {}).get('model_temperature')
    )

    use_token_usage = (
        token_usage
        if token_usage is not None
        else config.get('settings', {}).get('token_usage')
    )

    output_path = output_file or config.get('settings', {}).get('output_file')

    task_args = {
        'repo_url': github_repository_url,
    }

    if selected_model is not None:
        task_args['selected_model'] = selected_model
    if temperature_setting is not None:
        task_args['temperature_setting'] = temperature_setting
    if output_path is not None:
        task_args['output_file'] = output_path
    if use_token_usage is not None:
        task_args['token_usage'] = use_token_usage

    try:
        asyncio.run(process_repository_tasks(**task_args))
    except Exception as e:
        handle_error(e)


@app.command(
    name='init',
    help="Create the .github-echo.toml config file in the user's home directory.",
)
def create_config():
    home_directory = Path.home()
    config_file_path = home_directory / _constants.CONFIG_FILE

    if config_file_path.exists():
        console.print(
            f'[bold yellow]Config file already exists at {config_file_path}[/]'
        )
        return

    try:
        config_file_path.write_text(_constants.DEFAULT_CONFIG.strip())
        console.print(
            f'[bold green]Config file created successfully at {config_file_path}[/]'
        )
    except Exception as e:
        console.print(f'[bold red]Error creating config file: {e}[/]')


@app.command(
    name='remove-config',
    help="Remove the .github-echo.toml configuration file from the user's home directory.",
)
def remove_config():
    """
    Removes the .github-echo configuration file from the user's home directory if it exists.
    """
    home_directory = Path.home()
    config_file_path = home_directory / _constants.CONFIG_FILE

    if not config_file_path.exists():
        console.print(
            f'[bold yellow]Config file not found at {config_file_path}[/]'
        )
        return

    try:
        config_file_path.unlink()
        console.print(
            f'[bold red]Config file removed successfully at {config_file_path}[/]'
        )
    except Exception as e:
        console.print(f'[bold red]Error removing config file: {e}[/]')


if __name__ == '__main__':
    app()
