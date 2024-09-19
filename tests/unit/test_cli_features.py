import subprocess


def test_version(run_command: callable) -> None:
    """
    Test to verify that the command-line tool returns the correct version number.

    Args:
        run_command (callable): A function to execute command-line tools or scripts.

    Returns:
        None
    """
    result: subprocess.CompletedProcess = run_command("-v")

    assert result.returncode == 0
    assert "github-echo version 0.2.0" in result.stdout
