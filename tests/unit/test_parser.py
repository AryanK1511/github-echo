from pathlib import Path
from typing import Dict
from unittest.mock import patch

import pytest

from application.utils.parser import (
    format_category_name,
    json_to_markdown,
    load_toml_config,
    parse_github_url,
)


class TestLoadTomlConfig:
    @pytest.fixture
    def config_file_content(self) -> str:
        return """
        github_repository_url = "https://github.com/username/repository"
        model = "gemini"
        model_temperature = 0.7
        output_file = "/path/to/output/results.md"
        token_usage = true
        """

    @pytest.fixture
    def expected_config(self) -> Dict:
        return {
            'github_repository_url': 'https://github.com/username/repository',
            'model': 'gemini',
            'model_temperature': 0.7,
            'output_file': '/path/to/output/results.md',
            'token_usage': True,
        }

    # Test successful loading of a valid TOML config file
    def test_load_valid_config(self, config_file_content, expected_config):
        with patch(
            'application.utils.parser.Path.home',
            return_value=Path('/mock/home'),
        ), patch('pathlib.Path.exists', return_value=True), patch(
            'builtins.open'
        ) as mock_file:
            mock_file.return_value.__enter__.return_value.read.return_value = (
                config_file_content
            )
            config = load_toml_config('.github-echo-config.toml')
            assert config == expected_config
            expected_path = Path('/mock/home/.github-echo-config.toml')
            mock_file.assert_called_once_with(expected_path)

    # Test handling of missing config file
    def test_load_missing_config_file(self):
        with patch(
            'application.utils.parser.Path.home',
            return_value=Path('/mock/home'),
        ), patch('pathlib.Path.exists', return_value=False):
            config = load_toml_config('.github-echo-config.toml')
            assert config == {}

    # Test handling of malformed TOML content
    def test_load_invalid_config_format(self):
        with patch(
            'application.utils.parser.Path.home',
            return_value=Path('/mock/home'),
        ), patch('pathlib.Path.exists', return_value=True), patch(
            'builtins.open'
        ) as mock_file:
            mock_file.return_value.__enter__.return_value.read.return_value = (
                'invalid toml format'
            )
            with pytest.raises(RuntimeError) as exc_info:
                load_toml_config('.github-echo-config.toml')
            assert 'Failed to load or parse the config file' in str(
                exc_info.value
            )

    # Test handling of file read permission error
    def test_load_file_permission_error(self):
        with patch(
            'application.utils.parser.Path.home',
            return_value=Path('/mock/home'),
        ), patch('pathlib.Path.exists', return_value=True), patch(
            'builtins.open'
        ) as mock_file:
            mock_file.side_effect = PermissionError('Permission denied')
            with pytest.raises(PermissionError):
                load_toml_config('.github-echo-config.toml')

    # Test handling of empty config file
    def test_load_empty_config(self):
        with patch(
            'application.utils.parser.Path.home',
            return_value=Path('/mock/home'),
        ), patch('pathlib.Path.exists', return_value=True), patch(
            'builtins.open'
        ) as mock_file:
            mock_file.return_value.__enter__.return_value.read.return_value = (
                ''
            )
            config = load_toml_config('.github-echo-config.toml')
            assert config == {}

    # Test handling of file read errors
    def test_load_file_read_error(self):
        with patch(
            'application.utils.parser.Path.home',
            return_value=Path('/mock/home'),
        ), patch('pathlib.Path.exists', return_value=True), patch(
            'builtins.open'
        ) as mock_file:
            mock_file.return_value.__enter__.return_value.read.side_effect = (
                IOError('Read error')
            )
            with pytest.raises(IOError):
                load_toml_config('.github-echo-config.toml')

    # Test handling of partial/incomplete TOML content
    def test_load_partial_config(self):
        with patch(
            'application.utils.parser.Path.home',
            return_value=Path('/mock/home'),
        ), patch('pathlib.Path.exists', return_value=True), patch(
            'builtins.open'
        ) as mock_file:
            partial_content = 'github_repository_url = "https://github.com/username/repository"\n'
            mock_file.return_value.__enter__.return_value.read.return_value = (
                partial_content
            )
            config = load_toml_config('.github-echo-config.toml')
            assert config == {
                'github_repository_url': 'https://github.com/username/repository'
            }

    # Test handling of unicode characters in config
    def test_load_unicode_config(self):
        with patch(
            'application.utils.parser.Path.home',
            return_value=Path('/mock/home'),
        ), patch('pathlib.Path.exists', return_value=True), patch(
            'builtins.open'
        ) as mock_file:
            unicode_content = 'description = "测试 🚀 test"\n'
            mock_file.return_value.__enter__.return_value.read.return_value = (
                unicode_content
            )
            config = load_toml_config('.github-echo-config.toml')
            assert config == {'description': '测试 🚀 test'}


class TestFormatCategoryName:
    # Test formatting of a category name
    def test_format_category_name(self):
        result = format_category_name('github_repository')
        assert result == 'Github Repository'

    # Test category name with underscores only
    def test_format_category_name_single_word(self):
        result = format_category_name('github')
        assert result == 'Github'

    # Test category name with mixed-case words
    def test_format_category_name_mixed_case(self):
        result = format_category_name('user_repo')
        assert result == 'User Repo'


class TestParseGithubUrl:
    # Test valid GitHub URL parsing
    def test_parse_github_url_valid(self):
        username, repository = parse_github_url(
            'https://github.com/username/repository'
        )
        assert username == 'username'
        assert repository == 'repository'

    # Test invalid GitHub URL format
    def test_parse_github_url_invalid(self):
        with pytest.raises(ValueError) as exc_info:
            parse_github_url('https://github.com/username')
        assert 'Invalid GitHub URL format' in str(exc_info.value)

    # Test invalid GitHub URL (missing repository)
    def test_parse_github_url_missing_repo(self):
        with pytest.raises(ValueError) as exc_info:
            parse_github_url('https://github.com/username/')
        assert 'Invalid GitHub URL format' in str(exc_info.value)

    # Test GitHub URL with extra slashes
    def test_parse_github_url_extra_slashes(self):
        username, repository = parse_github_url(
            'https://github.com/username/repository//'
        )
        assert username == 'username'
        assert repository == 'repository'


class TestJsonToMarkdown:
    # Test valid JSON to Markdown conversion
    def test_json_to_markdown_valid(self):
        data = {
            'Insights': [
                {'title': 'Insight 1', 'description': 'Description 1'},
                {'title': 'Insight 2', 'description': 'Description 2'},
            ]
        }
        result = json_to_markdown(data)
        expected_result = (
            '## Insights\n'
            ' - **Insight 1**: Description 1\n'
            ' - **Insight 2**: Description 2\n\n'
        )
        assert result == expected_result

    # Test empty category
    def test_json_to_markdown_empty_category(self):
        data = {'Insights': []}
        result = json_to_markdown(data)
        assert result == ''

    # Test category with missing title or description
    def test_json_to_markdown_missing_title_or_description(self):
        data = {
            'Insights': [
                {'title': '', 'description': 'Description 1'},
                {'title': 'Insight 2', 'description': ''},
            ]
        }
        result = json_to_markdown(data)
        expected_result = ''
        assert result == expected_result

    # Test multiple categories with data
    def test_json_to_markdown_multiple_categories(self):
        data = {
            'Category 1': [
                {'title': 'Insight 1', 'description': 'Description 1'}
            ],
            'Category 2': [
                {'title': 'Insight 2', 'description': 'Description 2'}
            ],
        }
        result = json_to_markdown(data)
        expected_result = (
            '## Category 1\n'
            ' - **Insight 1**: Description 1\n\n'
            '## Category 2\n'
            ' - **Insight 2**: Description 2\n\n'
        )
        assert result == expected_result
