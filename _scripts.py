import subprocess


def lint():
    """Run Ruff linter and fix all the changes that can be fixed automatically"""
    subprocess.run(['ruff', 'check', '--fix'], check=True)


def format_code():
    """Format code with Ruff"""
    subprocess.run(['ruff', 'format'], check=True)


def lint_and_format():
    """Run both linting and formatting."""
    lint()
    format_code()
