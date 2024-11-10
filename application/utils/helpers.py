from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from single_source import get_version

from application.core.github_api import fetch_github_data
from application.core.models.gemini_model import get_gemini_summary
from application.core.models.groq_model import get_groq_summary
from application.utils.parser import parse_github_url
from application.utils.validation import check_cli_arguments

console = Console()
err_console = Console(stderr=True)


def get_cli_version(value: bool):
    """Handle the `--version` flag."""

    if value:
        __version__ = get_version(
            __name__, Path(__file__).parent.parent.parent
        )
        console.print(
            f'[bold bright_magenta]github-echo version[/bold bright_magenta] '
            f'{__version__}'
        )
        raise typer.Exit()


async def process_repository_tasks(
    repo_url: str,
    selected_model: Optional[str] = 'gemini',
    temperature_setting: Optional[float] = 0.5,
    output_file: Optional[Path] = None,
    token_usage: Optional[bool] = False,
):
    """Processes the provided GitHub repository URL and performs tasks
    to analyze the repository."""

    with Progress(
        SpinnerColumn(),
        TextColumn('[bold cyan][progress.description]{task.description}'),
        transient=True,
    ) as progress:
        check_cli_arguments(
            repo_url, selected_model, temperature_setting, output_file
        )
        console.print(
            f'[bold cyan][Model Selected][/bold cyan] '
            f'[bold yellow]{selected_model}[/bold yellow]\n'
            f'[bold cyan][Model Temperature][/bold cyan] '
            f'[bold yellow]{temperature_setting}[/bold yellow] '
            f'[italic dim](higher values are more random)[/italic dim]\n'
            f'[bold cyan][Display Token Usage Stats][/bold cyan] '
            f'[bold yellow]{token_usage}[/bold yellow]'
            f'\n'
        )

        task = progress.add_task(description='Processing...', total=None)

        # Task 01: Parse the GitHub URL
        progress.update(task, description='Parsing URL...')
        repo_owner, repo_name = parse_github_url(repo_url)

        # Task 02: Fetch GitHub data
        progress.update(task, description='Fetching data...', completed=1)
        repo_data_json = await fetch_github_data(repo_owner, repo_name)

        # Task 03: Generate summary
        progress.update(task, description='Generating summary...', completed=2)
        response = get_summary_based_on_model(
            repo_data_json, selected_model, temperature_setting
        )

        await handle_summary_output(response, output_file, token_usage)


def get_summary_based_on_model(
    repo_data_json, selected_model, temperature_setting
):
    """Generates the summary based on the selected model."""

    if selected_model == 'groq':
        return get_groq_summary(repo_data_json, temperature_setting)
    return get_gemini_summary(repo_data_json, temperature_setting)


async def handle_summary_output(response, output_file, token_usage):
    """Handles output of the generated summary."""

    usage = response['usage']
    repo_summary = response['formatted_response']

    if output_file:
        with open(output_file, 'w') as file:
            file.write(repo_summary)
        console.print(
            f'\n\n:sparkles: [bold]Summary written to '
            f'[bold cyan]{output_file}[/bold cyan].'
        )
    else:
        console.print(
            '\n\n:sparkles: [bold]Task completed! Here is the generated '
            'summary:'
        )
        console.print(Markdown(repo_summary))

    if token_usage:
        print_token_usage(usage)


def print_token_usage(usage):
    """Prints the token usage."""

    formatted_usage = (
        '\n[bold green]Token Usage:[/bold green]\n[bold yellow]-------------'
        '[/bold yellow]\n'
    )
    if 'candidates_token_count' in usage:  # For Gemini
        formatted_usage += (
            f'- [cyan]Completion Tokens:[/cyan] '
            f'[bold]{usage.candidates_token_count}[/bold]\n'
            f'- [cyan]Prompt Tokens:[/cyan] [bold]{usage.prompt_token_count}[/bold]\n'
            f'- [cyan]Total Tokens:[/cyan] [bold]{usage.total_token_count}[/bold]\n'
        )
    else:  # For Groq
        formatted_usage += (
            f'- [cyan]Completion Tokens:[/cyan] [bold]{usage.completion_tokens}[/bold]\n'
            f'- [cyan]Prompt Tokens:[/cyan] [bold]{usage.prompt_tokens}[/bold]\n'
            f'- [cyan]Total Tokens:[/cyan] [bold]{usage.total_tokens}[/bold]\n'
        )
    err_console.print(formatted_usage)


def handle_error(e):
    """Handles errors during processing."""

    err_console.print('\n[red]🚨 [bold]Error[/bold] 🚨\n')
    err_console.print(f'[red]{e}[/red]\n')
    err_console.print(
        '[bold yellow]Tip:[/bold yellow] Use '
        '[bold bright_magenta]github-echo --help[/bold bright_magenta] for '
        'usage information.\n'
    )
    err_console.print(
        '[bold green]For more help, refer to the project README File.\n'
    )
    raise typer.Exit(code=1)
