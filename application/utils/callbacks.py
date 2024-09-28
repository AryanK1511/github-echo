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

# Console instances for standard and error output
console = Console()
err_console = Console(stderr=True)


def version_callback(value: bool):
    """
    Callback function to handle the `--version` flag.
    Prints the version number and exits the application if the flag is provided.
    """
    if value:
        __version__ = get_version(__name__, Path(__file__).parent.parent.parent)
        console.print(
            f"[bold bright_magenta]github-echo version[/bold bright_magenta] {__version__}"
        )
        raise typer.Exit()


async def process_tasks(
    github_repository_url: str,
    model: Optional[str] = "gemini",  # Default model is gemini
    model_temperature: Optional[float] = None,
    output_file: Optional[Path] = None,
    token_usage: Optional[bool] = False,
):
    """
    Processes the provided GitHub repository URL and performs tasks to analyze the repository.

    Args:
        github_repository_url (str): The URL of the GitHub repository to analyze.
        model (Optional[str]): The model to use for generating insights.
        model_temperature (Optional[float]): Temperature setting for the model.
        output_file (Optional[Path]): Optional path to an output file where the Markdown summary will be written.
        token_usage (Optional[bool]): Flag to indicate if token usage should be printed.
    """

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan][progress.description]{task.description}"),
        transient=True,
    ) as progress:
        # Validate all the arguments provided by the user before trying to run any of the other operations
        check_cli_arguments(
            github_repository_url, model, model_temperature, output_file
        )

        # Logging the model details: name and temperature
        console.print(
            f"[bold cyan][Model Selected][/bold cyan] [bold yellow]{model}[/bold yellow]\n[bold cyan][Model Temperature][/bold cyan] [bold yellow]{model_temperature}[/bold yellow] [italic dim](controls the creativity of responses; higher values are more random)[/italic dim]"
        )
        task = progress.add_task(description="Processing...", total=None)

        # Task 01 -> Parse the GitHub URL and extract the owner and repo name
        progress.update(task, description="Parsing URL...")
        github_username, github_repository_name = parse_github_url(
            github_repository_url
        )

        # Task 02 -> Fetch the GitHub data asynchronously
        progress.update(task, description="Fetching data...", completed=1)
        repo_data_json = await fetch_github_data(
            github_username, github_repository_name
        )

        # Task 03 -> Generate the summary based on the selected model
        progress.update(task, description="Generating summary...", completed=2)

        if model == "groq":
            response = get_groq_summary(repo_data_json, model_temperature)
        else:  # Default to gemini
            response = get_gemini_summary(repo_data_json, model_temperature)

        usage = response["usage"]
        repo_summary = response["formatted_response"]

        # Display a message to the user
        completion_message = (
            ":sparkles: [bold]Task completed! Here is the generated summary:"
        )

        if output_file:
            # Write the summary to the file
            with open(output_file, "w") as file:
                file.write(repo_summary)
            console.print(
                f"\n\n:sparkles: [bold]Summary written to [bold cyan]{output_file}[/bold cyan]."
            )
        else:
            # Render the summary in markdown format and print to the terminal
            console.print(f"\n\n{completion_message}")
            md = Markdown(repo_summary)
            console.print(md)

        # If token_usage argument is specified, print the usage
        if token_usage:
            formatted_usage = (
                "\n[bold green]Token Usage:[/bold green]\n"
                "[bold yellow]-------------[/bold yellow]\n"
            )

            if model == "gemini":
                formatted_usage += (
                    f"- [cyan]Completion Tokens:[/cyan] [bold]{usage.candidates_token_count}[/bold]\n"
                    f"- [cyan]Prompt Tokens:[/cyan] [bold]{usage.prompt_token_count}[/bold]\n"
                    f"- [cyan]Total Tokens:[/cyan] [bold]{usage.total_token_count}[/bold]\n"
                )
            elif model == "groq":
                formatted_usage += (
                    f"- [cyan]Completion Tokens:[/cyan] [bold]{usage.completion_tokens}[/bold]\n"
                    f"- [cyan]Prompt Tokens:[/cyan] [bold]{usage.prompt_tokens}[/bold]\n"
                    f"- [cyan]Total Tokens:[/cyan] [bold]{usage.total_tokens}[/bold]\n"
                )

            err_console.print(formatted_usage)
