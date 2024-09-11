import asyncio
import time
from pathlib import Path
from typing import Optional

import toml
import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import BarColumn, Progress, TextColumn

from application.core.gemini_model import get_gemini_summary
from application.core.github_api import fetch_github_data
from application.utils.parser import parse_github_url

# Console instances for standard and error output
console = Console(soft_wrap=True)
err_console = Console(stderr=True, soft_wrap=True)


def version_callback(value: bool):
    """
    Callback function to handle the `--version` flag.
    Prints the version number and exits the application if the flag is provided.
    """
    pyproject = toml.load("pyproject.toml")
    if value:
        console.print(
            f"[bold bright_magenta]github-echo version[/bold bright_magenta] {pyproject['tool']['poetry']['version']}"
        )
        raise typer.Exit()


def process_tasks(github_repository_url: str, output_file: Optional[Path]):
    """
    Processes the provided GitHub repository URL and performs tasks to analyze the repository.

    Args:
        github_repository_url (str): The URL of the GitHub repository to analyze.
        output_file (Optional[Path]): Optional path to an output file where the Markdown summary will be written.
    """

    # Define the total number of tasks to be completed
    total_tasks = 3

    with Progress(
        TextColumn(
            "[bold cyan]🔍 [Analyzing repository for insights...]", justify="right"
        ),
        BarColumn(bar_width=60, pulse_style="bright_magenta"),
        TextColumn(
            "[bold green][progress.percentage]{task.percentage:>3.0f}%", justify="right"
        ),
        transient=True,
    ) as progress:
        task = progress.add_task(" Analyzing Repository", total=total_tasks)

        # Task 01 -> Parse the GitHub URL and extract the owner and repo name
        github_username, github_repository_name = parse_github_url(
            github_repository_url
        )
        progress.advance(task)
        time.sleep(0.3)

        # Task 02 -> Fetch the GitHub data asynchronously
        repo_data_json = asyncio.run(
            fetch_github_data(github_username, github_repository_name)
        )

        progress.advance(task)
        time.sleep(0.3)

        # Task 03 -> Generate the Gemini summary
        repo_summary = get_gemini_summary(repo_data_json)
        progress.advance(task)
        time.sleep(0.3)
        progress.update(task, completed=total_tasks)
        time.sleep(0.3)

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
