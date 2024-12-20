import json
from typing import Any, Dict

from groq import Groq

from _config import GROQ_API_KEY
from application.utils.model_config import (
    GROQ_MODEL,
    SYSTEM_INSTRUCTION,
    generate_prompt,
)
from application.utils.parser import json_to_markdown

GROQ_API_KEY = GROQ_API_KEY if GROQ_API_KEY else ''

client = None
try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    raise RuntimeError(
        f'Failed to configure the Groq GenAI API: {str(e)}'
    ) from e


def get_groq_summary(
    repo_data: Dict[str, Any], temperature: float
) -> Dict[str, Any]:
    """
    Generates a summary of the repository data using the Groq model.
    """
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {'role': 'system', 'content': SYSTEM_INSTRUCTION},
                {'role': 'user', 'content': f'{generate_prompt(repo_data)}'},
            ],
            response_format={'type': 'json_object'},
            temperature=temperature,
            stream=False,
        )

        json_response = json.loads(response.choices[0].message.content)
        formatted_response = json_to_markdown(json_response)

        return {
            'formatted_response': formatted_response,
            'usage': response.usage,
        }

    except Exception as e:
        raise RuntimeError(
            f'Failed to generate summary using groq: {str(e)}'
        ) from e
