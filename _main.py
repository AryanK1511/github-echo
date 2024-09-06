#!/usr/bin/env python3

import typer
from rich import print

from application.utils.gemini_model import response

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")
    print(response.text)
    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


if __name__ == "__main__":
    app()
