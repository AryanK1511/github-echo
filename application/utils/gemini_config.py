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

"""
    * candidateCount specifies the number of generated responses to return. If unset, this will default to 1.

    * stopSequences specifies the set of character sequences (up to 5) that will stop output generation. If specified, the API will stop at the first appearance of a stop_sequence. The stop sequence won't be included as part of the response.

    * maxOutputTokens sets the maximum number of tokens to include in a candidate.

    * temperature controls the randomness of the output. Use higher values for more creative responses, and lower values for more deterministic responses. Values can range from [0.0, 2.0].
"""

GENERATION_CONFIG = (
    genai.types.GenerationConfig(
        candidate_count=1,
        temperature=1.0,
    ),
)
