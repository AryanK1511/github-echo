import json
from typing import Any, Dict

import google.generativeai as genai

from _config import GOOGLE_GEMINI_API_KEY
from application.utils.model_config import (
    GEMINI_MODEL,
    SYSTEM_INSTRUCTION,
    generate_prompt,
    get_gemini_generation_config,
)
from application.utils.parser import json_to_markdown

try:
    genai.configure(api_key=GOOGLE_GEMINI_API_KEY)
except Exception as e:
    raise Exception(
        'Failed to configure the Gemini GenAI API. Check whether the API key is valid.'
    ) from e

model = genai.GenerativeModel(
    model_name=GEMINI_MODEL, system_instruction=SYSTEM_INSTRUCTION
)


def get_gemini_summary(
    github_data: Dict[str, Any], model_temperature: float
) -> Dict[str, Any]:
    """
    Generates a summary of the GitHub repository data using the Gemini model.
    """
    try:
        response = model.generate_content(
            f'{generate_prompt(github_data)}',
            generation_config=get_gemini_generation_config(
                temperature=model_temperature
            ),
        )

        json_response = json.loads(response.text)
        formatted_response = json_to_markdown(json_response)

        return {
            'formatted_response': formatted_response,
            'usage': response.usage_metadata,
        }

    except Exception as e:
        raise RuntimeError(
            f'Failed to generate summary using gemini: {str(e)}'
        ) from e
