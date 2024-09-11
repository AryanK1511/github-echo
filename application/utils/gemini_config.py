# This file cotains parameters that are used to configure gemini to our use case
import google.generativeai as genai

"""
* gemini-1.0-flash -> Ideal for text inputs
* Natural language tasks, multi-turn text and code chat, and code generation
* Available gemini models: https://ai.google.dev/gemini-api/docs/models/gemini
"""

GEMINI_MODEL = "gemini-1.5-flash"

GEMINI_SYSTEM_INSTRUCTION = (
    " You are a software developer wanting to contribute to open source. \
    You have been tasked with analyzing a GitHub repository to provide insights on its development trends, community engagement, release cadence, code base composition, repository popularity, and branch protection rules.\
    Your task is to generate a summary based on the GitHub Repository data given. What would you want to know as a contributor.\
    "
)

GEMINI_PROMPT = (
    "Given the GitHub repository data, provide an in-depth analysis with the following insights:\
    Contribution Trends:\
        - Analyze the commit frequency and identify any significant trends or patterns in repository development.\
        - Assess contributor activity trends and correlate them with any major repository events or changes.\
        - Mention what kind of changes or features are the contributors working on right now.\
    Community Engagement:\
        - Evaluate the average time taken to resolve issues and merge pull requests. Compare these metrics with overall repository activity.\
        - Determine the impact of individual contributors on issue resolution and code changes.\
    Release Cadence:\
        - Examine the frequency and timing of releases. Identify any patterns in release cycles or versioning practices.\
    Code Base Composition:\
        - Provide insights into language usage trends and their evolution over time.\
        - Assess the health and stability of dependencies, noting any potential security concerns.\
    Repository Popularity:\
        - Analyze repository traffic data and correlate it with stars, forks, and watchers to gauge growth in popularity.\
    Branch Protection:\
        - Evaluate the branch protection rules in place and their implications for code quality and collaboration.\
    Potential Changed that a contributor can make:\
        - Identify areas of the codebase that are most in need of contributions or improvements.\
    Generate a summary that highlights key trends, anomalies, and actionable insights. Generate it in Markdown and proper formatting so that its easier to read. Make it concise but be sure to have quantifiable numbers.\
"
)


def get_gemini_generation_config(
    candidate_count=1, temperature=1.0, stop_sequences=None, max_output_tokens=None
):
    """
    Creates a GenerationConfig object with specified parameters for generating responses.

    Parameters:
        candidate_count (int): The number of responses to generate. Must be an integer greater than or equal to 1. Default is 1.
        temperature (float): Controls the randomness of the output. Must be a float or integer between 0.0 and 2.0. Default is 1.0.
        stop_sequences (list of str, optional): A list of up to 5 character sequences that, if encountered, will stop output generation. Default is None, which means no stop sequences are applied. Each sequence must be a string.
        max_output_tokens (int, optional): The maximum number of tokens to include in a response. Must be an integer greater than or equal to 1. Default is None, which means no limit is applied.

    Returns:
        genai.types.GenerationConfig: An instance of GenerationConfig with the provided settings.
    """

    # Validate candidate_count
    if not isinstance(candidate_count, int) or candidate_count < 1:
        raise ValueError(
            "candidate_count must be an integer greater than or equal to 1."
        )

    # Validate temperature
    if not (isinstance(temperature, float) or isinstance(temperature, int)):
        raise TypeError("temperature must be a float or integer.")
    if not (0.0 <= temperature <= 2.0):
        raise ValueError("temperature must be between 0.0 and 2.0.")

    # Validate stop_sequences
    if stop_sequences is not None:
        if not isinstance(stop_sequences, list):
            raise TypeError("stop_sequences must be a list.")
        if len(stop_sequences) > 5:
            raise ValueError("stop_sequences list cannot have more than 5 items.")
        if not all(isinstance(seq, str) for seq in stop_sequences):
            raise TypeError("All items in stop_sequences must be strings.")

    # Validate max_output_tokens
    if max_output_tokens is not None:
        if not isinstance(max_output_tokens, int) or max_output_tokens < 1:
            raise ValueError(
                "max_output_tokens must be an integer greater than or equal to 1."
            )

    return genai.types.GenerationConfig(
        candidate_count=candidate_count,
        temperature=temperature,
        stop_sequences=stop_sequences or [],
        max_output_tokens=max_output_tokens,
    )
