#!/usr/bin/env python3

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from typing_extensions import Annotated

from application.utils.callbacks import process_tasks, version_callback

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
    output_file: Annotated[
        Optional[Path], typer.Option("--output", "-o", help="Path to the output file")
    ] = None,
):
    """
    Main function to analyze a GitHub repository and optionally output the results to a file.

    Args:
        github_repository_url (str): Required. The URL of the GitHub repository to analyze.
        version (Optional[bool]): Optional. If provided, prints the version number and exits the application.
        output_file (Optional[Path]): Optional. If provided, the path to a file where the Markdown summary will be saved.
    """
    try:
        process_tasks(github_repository_url, output_file)
    except Exception as e:
        err_console.print("\n[bold red]🚨 Something went wrong![/bold red]\n")
        err_console.print(f"[red]💡 [bold]Error:[/bold] {e}\n", highlight=True)
        err_console.print(
            "[bold yellow]Tip:[/bold yellow] Ensure the GitHub URL is valid, Environment variables are set up, and your internet connection is stable.\n"
        )
        err_console.print(
            "[bold green]For more information, please refer to the project README File.\n"
        )
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
