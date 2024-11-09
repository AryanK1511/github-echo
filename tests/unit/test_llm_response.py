import json
from unittest.mock import MagicMock, patch

import pytest

from application.core.models.gemini_model import get_gemini_summary
from application.core.models.groq_model import get_groq_summary
from application.utils.parser import json_to_markdown


class TestGeminiSummary:
    @pytest.fixture
    def mock_gemini_response(self):
        return {
            'branch_protection': [
                {
                    'title': 'Branch Protection Rules Missing',
                    'description': (
                        'The repository currently lacks branch protection rules. '
                        'Implementing rules such as requiring code reviews, testing, '
                        'and approvals before merging changes can significantly enhance '
                        'code quality and prevent accidental deployments.'
                    ),
                }
            ],
            'code_base_composition': [
                {
                    'title': 'Dominant Language: Python',
                    'description': (
                        'Python is the primary language used in the repository, '
                        'accounting for 93% of the codebase. This indicates a focus '
                        "on scripting and automation, which aligns well with the project's "
                        'purpose as a command-line tool.'
                    ),
                },
                {
                    'title': 'Dockerfile Usage',
                    'description': (
                        'The presence of a Dockerfile suggests the repository utilizes '
                        'containerization for deployment and development environments. '
                        'This can simplify setup and promote consistency across different systems.'
                    ),
                },
                {
                    'title': 'Dependency Management',
                    'description': (
                        'The repository does not explicitly mention its dependency management '
                        'strategy. Implementing a robust dependency management system like '
                        'pipenv or poetry can improve project maintainability and reduce '
                        'potential security vulnerabilities.'
                    ),
                },
            ],
            'community_engagement': [
                {
                    'title': 'Active Development',
                    'description': (
                        'The absence of open issues and pull requests suggests a well-maintained '
                        'codebase and a project with few outstanding issues. This indicates a '
                        'potentially strong community engagement.'
                    ),
                }
            ],
            'contribution_trends': [
                {
                    'title': 'Active Maintainer',
                    'description': (
                        'The commit history reveals consistent contributions from the primary '
                        'developer, Aryan Khurana, suggesting ongoing development and maintenance.'
                    ),
                },
                {
                    'title': 'Collaboration with Contributors',
                    'description': (
                        'The repository benefits from contributions from multiple developers, '
                        'including Fahad Ali Khan and Harshil Patel, indicating a collaborative '
                        'development environment.'
                    ),
                },
                {
                    'title': 'Burst of Activity',
                    'description': (
                        'A significant increase in commit activity occurred around October 4th, '
                        '2024, potentially related to a major feature release or bug fix.'
                    ),
                },
            ],
            'potential_changes': [
                {
                    'title': 'Expand Documentation',
                    'description': (
                        'The repository could benefit from more comprehensive documentation, '
                        'including detailed explanations of functionalities, usage examples, '
                        'and potential use cases for the tool.'
                    ),
                },
                {
                    'title': 'Implement CI/CD',
                    'description': (
                        'Integrating Continuous Integration and Continuous Deployment (CI/CD) '
                        'pipelines can automate testing, code quality checks, and deployments, '
                        'improving the development workflow'
                    ),
                },
                {
                    'title': 'Enhance Testing Suite',
                    'description': (
                        'Expanding the existing test suite to cover a broader range of scenarios '
                        'and functionalities can improve code robustness and maintainability.'
                    ),
                },
            ],
            'release_cadence': [
                {
                    'title': 'Regular Releases',
                    'description': (
                        'The repository follows a regular release cadence, with three releases '
                        '(v0.1.1, v0.2.0, and v0.3.0) documented in the past two months. This '
                        'indicates a commitment to delivering updates and improvements to users.'
                    ),
                },
                {
                    'title': 'Versioning Scheme',
                    'description': (
                        'The repository uses semantic versioning, which provides clear information '
                        'about the nature and scope of changes in each release.'
                    ),
                },
            ],
            'repository_popularity': [
                {
                    'title': 'Moderate Popularity',
                    'description': (
                        'The repository has a moderate level of popularity, with 14 stars, 14 '
                        'watchers, and 5 forks. This indicates a growing interest in the tool '
                        'and potential for further growth.'
                    ),
                }
            ],
            'summary': [
                {
                    'title': 'Healthy and Growing Repository',
                    'description': (
                        'The repository exhibits a healthy development environment with regular '
                        'releases, active maintenance, and a collaborative community. The moderate '
                        'popularity suggests potential for further growth, '
                        'especially with expanded '
                        'documentation and CI/CD integration.'
                    ),
                }
            ],
        }

    @pytest.fixture
    def mock_usage_metadata(self):
        return {
            'prompt_token_count': 11161,
            'candidates_token_count': 774,
            'total_token_count': 11935,
        }

    # Tests successful generation of summary using Gemini model
    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_get_gemini_summary(
        self, mock_generate_content, mock_gemini_response, mock_usage_metadata
    ):
        mock_response = MagicMock()
        mock_response.text = json.dumps(mock_gemini_response)
        mock_response.usage_metadata = mock_usage_metadata
        mock_generate_content.return_value = mock_response

        github_data = {'repo_name': 'example-repo', 'owner': 'user'}
        model_temperature = 0.7
        result = get_gemini_summary(github_data, model_temperature)

        expected_formatted_response = json_to_markdown(mock_gemini_response)
        assert result['formatted_response'] == expected_formatted_response
        assert result['usage'] == mock_usage_metadata

    # Tests error handling in Gemini summary generation
    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_get_gemini_summary_handles_error(self, mock_generate_content):
        mock_generate_content.side_effect = Exception('API call failed')

        with pytest.raises(
            RuntimeError, match='Failed to generate summary using gemini'
        ):
            get_gemini_summary(
                {'repo_name': 'example-repo', 'owner': 'user'}, 0.7
            )


class TestGroqSummary:
    @pytest.fixture
    def mock_claude_response(self):
        return {
            'branch_protection': [
                {
                    'title': 'No branch protection',
                    'description': (
                        'Currently, there are no branch protection rules set up '
                        'in the repository, such as required reviews or tests. '
                        'Enforcing CI checks and setting up required reviews '
                        'could benefit code quality.'
                    ),
                }
            ],
            'code_base_composition': [
                {
                    'title': 'Primary language and dependencies',
                    'description': (
                        'The main language of the repository is MDX, followed '
                        'by TypeScript, CSS, and JavaScript. There is no '
                        'information available about dependency health.'
                    ),
                }
            ],
        }

    @pytest.fixture
    def mock_groq_client(self, mock_claude_response):
        mock_client = MagicMock()
        mock_choice = MagicMock()
        mock_choice.message.content = json.dumps(mock_claude_response)

        mock_response = MagicMock()
        mock_response.choices = [mock_choice]
        mock_response.usage = {
            'completion_tokens': 123,
            'prompt_tokens': 456,
            'total_tokens': 579,
        }

        mock_client.chat.completions.create.return_value = mock_response
        return mock_client

    @pytest.fixture
    def mock_groq_client_error(self):
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = Exception(
            'API request failed'
        )
        return mock_client

    # Tests successful generation of summary using Groq model
    def test_get_groq_summary(self, mock_groq_client):
        with patch(
            'application.core.models.groq_model.client', mock_groq_client
        ):
            repo_data = {'some_key': 'some_value'}
            temperature = 0.5
            result = get_groq_summary(repo_data, temperature)

            mock_groq_client.chat.completions.create.assert_called_once()
            call_args = mock_groq_client.chat.completions.create.call_args[1]

            assert call_args['model'] == 'mixtral-8x7b-32768'
            assert len(call_args['messages']) == 2
            assert call_args['messages'][0]['role'] == 'system'
            assert call_args['messages'][1]['role'] == 'user'
            assert call_args['response_format'] == {'type': 'json_object'}
            assert call_args['temperature'] == temperature
            assert call_args['stream'] is False

            assert 'formatted_response' in result
            assert 'usage' in result

            formatted_response = result['formatted_response']
            assert '## Branch Protection' in formatted_response
            assert 'No branch protection' in formatted_response

    # Tests error handling in Groq summary generation
    def test_get_groq_summary_error(self, mock_groq_client_error):
        with patch(
            'application.core.models.groq_model.client', mock_groq_client_error
        ):
            repo_data = {'some_key': 'some_value'}
            temperature = 0.5

            with pytest.raises(RuntimeError) as exc_info:
                get_groq_summary(repo_data, temperature)

            assert 'Failed to generate summary using groq' in str(
                exc_info.value
            )
