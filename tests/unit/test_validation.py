from pathlib import Path

import pytest
import typer

from application.utils.validation import check_cli_arguments


class TestCheckCliArguments:
    # Test with all valid arguments
    def test_valid_arguments(self):
        github_url = 'https://github.com/username/repository'
        model = 'gemini'
        model_temperature = 0.5
        output_file = Path('output.md')

        check_cli_arguments(github_url, model, model_temperature, output_file)

    @pytest.mark.parametrize(
        'invalid_url',
        [
            'https://gitlab.com/username/repository',
            'https://github.com/username',
            'github.com/username/repository',
            'https://github.com//repository',
            'https://github.com/username/',
        ],
    )

    # Test invalid GitHub URL patterns
    def test_invalid_github_url(self, invalid_url):
        with pytest.raises(
            typer.BadParameter, match='Invalid GitHub repository URL'
        ):
            check_cli_arguments(invalid_url, 'gemini', 0.5, Path('output.md'))

    # Test when model is not specified
    def test_missing_model(self):
        github_url = 'https://github.com/username/repository'

        with pytest.raises(
            typer.BadParameter, match='Model must be specified'
        ):
            check_cli_arguments(github_url, None, 0.5, Path('output.md'))

    # Test invalid model input
    def test_invalid_model(self):
        github_url = 'https://github.com/username/repository'

        with pytest.raises(typer.BadParameter, match='Invalid model'):
            check_cli_arguments(
                github_url, 'unknown_model', 0.5, Path('output.md')
            )

    # Test when model temperature is not specified
    def test_missing_model_temperature(self):
        github_url = 'https://github.com/username/repository'

        with pytest.raises(
            typer.BadParameter, match='Model temperature must be specified'
        ):
            check_cli_arguments(github_url, 'gemini', None, Path('output.md'))

    # Test model temperature out of range (not between 0 and 1)
    @pytest.mark.parametrize('invalid_temperature', [-0.1, 1.1])
    def test_invalid_model_temperature(self, invalid_temperature):
        github_url = 'https://github.com/username/repository'

        with pytest.raises(
            typer.BadParameter, match='Invalid model temperature'
        ):
            check_cli_arguments(
                github_url, 'gemini', invalid_temperature, Path('output.md')
            )

    # Test when output file path is a directory instead of a file
    def test_output_file_is_directory(self, tmp_path):
        github_url = 'https://github.com/username/repository'
        output_dir = tmp_path

        with pytest.raises(
            typer.BadParameter, match='Invalid output file.*directory'
        ):
            check_cli_arguments(github_url, 'gemini', 0.5, output_dir)

    # Test when output file's parent directory does not exist
    def test_output_file_parent_directory_does_not_exist(self):
        github_url = 'https://github.com/username/repository'
        output_file = Path('non_existent_dir/output.md')

        with pytest.raises(
            typer.BadParameter, match='Invalid output file path'
        ):
            check_cli_arguments(github_url, 'gemini', 0.5, output_file)
