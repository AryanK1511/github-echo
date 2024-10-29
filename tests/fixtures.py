import os
import subprocess
from typing import List

import pytest


@pytest.fixture
def run_command() -> callable:
    """
    Fixture to run command-line tools or scripts from the root of the repository.

    Returns:
        function: A function that takes command-line arguments and returns
                  the result of the executed command.
    """

    def _run_command(*args: str) -> subprocess.CompletedProcess:
        repo_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..')
        )
        command: List[str] = ['python3', '_main.py'] + list(args)
        result = subprocess.run(
            command, cwd=repo_root, capture_output=True, text=True
        )

        return result

    return _run_command
