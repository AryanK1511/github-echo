import subprocess


def lint():
    """Run Ruff linter and fix all the changes that can be fixed automatically."""
    subprocess.run(['ruff', 'check', '--fix'], check=True)


def format_code():
    """Format code with Ruff."""
    subprocess.run(['ruff', 'format'], check=True)


def lint_and_format():
    """Run both linting and formatting."""
    lint()
    format_code()


def run_tests():
    """Run all tests using pytest."""
    subprocess.run(['pytest'], check=True)


def run_tests_on_files(files):
    """Run tests on specific file or files."""
    subprocess.run(['pytest', *files], check=True)


def run_tests_on_classes(classes):
    """Run tests on specific class or classes."""
    for class_name in classes:
        subprocess.run(['pytest', '-k', class_name], check=True)


def run_coverage():
    """Run tests with coverage reporting."""
    subprocess.run(['coverage', 'run', '-m', 'pytest'], check=True)


def run_coverage_report():
    """Generate and display coverage report."""
    subprocess.run(['coverage', 'report'], check=True)


def run_coverage_html():
    """Generate HTML coverage report."""
    subprocess.run(['coverage', 'html'], check=True)


def watch_tests():
    """Run tests in watch mode using pytest-watch."""
    subprocess.run(['ptw'], check=True)


def watch_tests_with_coverage():
    """Run tests in watch mode with coverage."""
    subprocess.run(['ptw', '--runner', 'coverage run -m pytest'], check=True)
