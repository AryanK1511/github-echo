from typing import Dict

import google.generativeai as genai

# Define the model and system instruction
GEMINI_MODEL = "gemini-1.5-flash"

GEMINI_SYSTEM_INSTRUCTION = """
You are a software developer analyzing a GitHub repository. Your task is to provide actionable insights into various aspects of the repository including development trends, community engagement, release cadence, code base composition, repository popularity, branch protection rules, and potential improvements. What key information would you need to provide useful insights?
"""

# Define prompts for each category of insights
CATEGORY_PROMPTS: Dict[str, str] = {
    "contribution_trends": """
    Analyze the commit frequency and identify significant trends or patterns in development. Assess contributor activity and correlate it with major repository events.
    """,
    "community_engagement": """
    Evaluate average issue resolution times and pull request merges. Determine the impact of contributors on these metrics.
    """,
    "release_cadence": """
    Examine release frequency and timing. Identify patterns in release cycles or versioning.
    """,
    "code_base_composition": """
    Provide insights into language usage trends and dependency health. Note any potential security concerns.
    """,
    "repository_popularity": """
    Analyze repository traffic and correlate with stars, forks, and watchers to gauge popularity.
    """,
    "branch_protection": """
    Evaluate the current branch protection rules. Identify areas where protection is missing or could be improved. Suggest implementing rules like requiring code reviews, testing, and approvals before merging changes.
    """,
    "potential_changes": """
    Identify areas of the codebase needing contributions or improvements.
    """,
    "summary": """
    Summarize key insights from each category and provide an overall assessment of the repository's health and growth potential.
    """,
}


def generate_gemini_prompt(repo_data: Dict[str, str]) -> str:
    """
    Generates a prompt for the Gemini model based on the provided GitHub repository data.

    Parameters:
        repo_data (dict): A dictionary containing GitHub repository data.

    Returns:
        str: A prompt string formatted for the Gemini model.
    """
    return f"""
    Analyze the following GitHub repository data and provide structured insights:

        {repo_data}

    For each category, provide a list of key insights with the following requirements:
    - Each insight should include a title and a concise description.
    - Avoid duplication of insights.
    - Ensure each description is data-driven and actionable, including quantifiable numbers where applicable.

    **Categories and Prompts:**

    {CATEGORY_PROMPTS}

    Format your response as a JSON object with the following structure:
    '''json
    {{
      "branch_protection": [
        {{
          "title": "string",
          "description": "string"
        }}
      ],
      "code_base_composition": [
        {{
          "title": "string",
          "description": "string"
        }}
      ],
      "community_engagement": [
        {{
          "title": "string",
          "description": "string"
        }}
      ],
      "contribution_trends": [
        {{
          "title": "string",
          "description": "string"
        }}
      ],
      "potential_changes": [
        {{
          "title": "string",
          "description": "string"
        }}
      ],
      "release_cadence": [
        {{
          "title": "string",
          "description": "string"
        }}
      ],
      "repository_popularity": [
        {{
          "title": "string",
          "description": "string"
        }}
      ],
      "summary": [
        {{
          "title": "string",
          "description": "string"
        }}
      ]
    }}
    '''
    """


def get_gemini_generation_config(
    candidate_count=1, temperature=0.5, stop_sequences=None, max_output_tokens=None
):
    """
    Creates a GenerationConfig object with specified parameters for generating responses.

    Parameters:
        candidate_count (int): Number of responses to generate (integer ≥ 1). Default is 1.
        temperature (float): Controls randomness of output (0.0 to 2.0). Default is 0.5.
        stop_sequences (list of str, optional): Up to 5 sequences to stop generation. Default is None.
        max_output_tokens (int, optional): Maximum number of tokens in a response (integer ≥ 1). Default is None.

    Returns:
        genai.types.GenerationConfig: An instance of GenerationConfig with the provided settings.
    """
    if not isinstance(candidate_count, int) or candidate_count < 1:
        raise ValueError("candidate_count must be an integer ≥ 1.")

    if not isinstance(temperature, (float, int)) or not (0.0 <= temperature <= 1.0):
        raise ValueError("temperature must be between 0.0 and 1.0.")

    if stop_sequences is not None:
        if (
            not isinstance(stop_sequences, list)
            or len(stop_sequences) > 5
            or not all(isinstance(seq, str) for seq in stop_sequences)
        ):
            raise ValueError("stop_sequences must be a list of up to 5 strings.")

    if max_output_tokens is not None and (
        not isinstance(max_output_tokens, int) or max_output_tokens < 1
    ):
        raise ValueError("max_output_tokens must be an integer ≥ 1.")

    return genai.types.GenerationConfig(
        candidate_count=candidate_count,
        temperature=temperature,
        stop_sequences=stop_sequences or [],
        max_output_tokens=max_output_tokens,
        response_mime_type="application/json",
    )
