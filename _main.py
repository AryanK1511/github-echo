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
    model_temperature: Annotated[
        Optional[float],
        typer.Option(
            "--temperature",
            "-t",
            help="Sets the temperature for the model, with a range from 0.0 (more deterministic) to 2.0 (more random).",
        ),
    ] = 1.0,
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
        process_tasks(
            github_repository_url=github_repository_url,
            output_file=output_file,
            model_temperature=model_temperature,
        )
    except Exception as e:
        err_console.print("\n[bold red]🚨 Something went wrong![/bold red]\n")
        err_console.print(f"[red]💡 [bold]Error:[/bold] {e}\n", highlight=True)
        err_console.print(
            "[bold yellow]Tip:[/bold yellow] Use [bold bright_magenta]github-echo --help[/bold bright_magenta] to get usage information.\n"
        )
        err_console.print(
            "[bold green]For more help, please refer to the project README File.\n"
        )
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
