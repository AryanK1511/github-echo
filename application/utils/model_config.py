from typing import Dict

import google.generativeai as genai

# Define the models and system instruction
GEMINI_MODEL = 'gemini-1.5-flash'
GROQ_MODEL = 'mixtral-8x7b-32768'

SYSTEM_INSTRUCTION = """
You are a software developer analyzing a GitHub repository. Your task is to
provide concise, actionable insights into the repository’s development trends,
community engagement, release cadence, code base composition, popularity, branch
protection, and areas needing improvement. Use quantifiable metrics to help
determine if the repository is a good fit for new contributors.
"""

# Define refined prompts for each category of insights
CATEGORY_PROMPTS: Dict[str, str] = {
    'contribution_trends': """
    Identify trends in commit frequency, average commits per month, and any
    peak or dip periods. Highlight active contributors and any gaps in
    contribution history that may suggest high or low activity periods.
    """,
    'community_engagement': """
    Provide average issue response time and merge time for pull requests.
    Highlight tags like 'good first issue' and 'help wanted' and their usage
    frequency to indicate welcoming community practices.
    """,
    'release_cadence': """
    Examine the release pattern and version frequency. Identify if there is a
    consistent release schedule, and note any recent shifts in release frequency
    that could reflect changing priorities or stability.
    """,
    'code_base_composition': """
    Summarize primary language composition (top two or three languages by
    percentage) and dependency health. Identify any outdated or vulnerable
    dependencies to assess maintenance quality.
    """,
    'repository_popularity': """
    Analyze growth in stars, forks, and watchers over time. Provide traffic data
    (views, clones) to indicate active user interest. Correlate popular periods
    with key releases or updates.
    """,
    'branch_protection': """
    List current branch protection rules (e.g., required reviews, tests). Identify
    missing protections that could benefit code quality, such as enforcing CI checks.
    """,
    'potential_changes': """
    Highlight low-activity areas, outstanding enhancement requests, or any components
    lacking recent contributions where new contributors can add value.
    """,
    'summary': """
    Summarize top insights across categories, focusing on repository health,
    engagement level, and potential for growth. Provide an overall assessment
    for new contributors.
    """,
}


def generate_prompt(repo_data: Dict[str, str]) -> str:
    """
    Generates a prompt for the Gemini model based on the provided GitHub
    repository data, focusing on actionable and quantifiable insights.
    """

    return f"""
    Based on the following GitHub repository data, provide actionable insights:

        {repo_data}

    For each category, include:
    - Insight title and concise description.
    - Data-driven and actionable content, using quantifiable metrics.

    **Categories and Prompts:**

    {CATEGORY_PROMPTS}

    Format response as JSON with this structure:
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
    candidate_count=1,
    temperature=0.5,
    stop_sequences=None,
    max_output_tokens=None,
):
    """
    Creates a GenerationConfig object with specified parameters for
    generating responses.
    """

    if stop_sequences is not None and (
        not isinstance(stop_sequences, list)
        or len(stop_sequences) > 5
        or not all(isinstance(seq, str) for seq in stop_sequences)
    ):
        raise ValueError('stop_sequences must be a list of up to 5 strings.')

    if max_output_tokens is not None and (
        not isinstance(max_output_tokens, int) or max_output_tokens < 1
    ):
        raise ValueError('max_output_tokens must be an integer ≥ 1.')

    return genai.types.GenerationConfig(
        candidate_count=candidate_count,
        temperature=temperature,
        stop_sequences=stop_sequences or [],
        max_output_tokens=max_output_tokens,
        response_mime_type='application/json',
    )
