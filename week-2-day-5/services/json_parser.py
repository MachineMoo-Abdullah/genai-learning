import json
import re


REQUIRED_FIELDS = [
    "client_needs",
    "pain_points",
    "recommended_services",
    "key_benefits",
    "target_outcomes",
]


def parse_json_response(text):
    """
    Safely parse JSON returned by the LLM.

    Handles:
    - Normal JSON
    - Markdown JSON code blocks
    - Extra text surrounding JSON
    """

    if not text:
        raise ValueError("The AI returned an empty response.")

    text = text.strip()

    # Remove markdown code fences
    text = re.sub(r"^```json\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    try:
        data = json.loads(text)
    except json.JSONDecodeError:

        # Try extracting the first JSON object
        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("The AI returned invalid JSON.")

        try:
            data = json.loads(text[start:end + 1])
        except json.JSONDecodeError as exc:
            raise ValueError(
                "The AI returned malformed JSON."
            ) from exc

    if not isinstance(data, dict):
        raise ValueError("The AI JSON response must be an object.")

    missing = [
        field for field in REQUIRED_FIELDS
        if field not in data
    ]

    if missing:
        raise ValueError(
            f"AI JSON is missing required fields: {', '.join(missing)}"
        )

    for field in REQUIRED_FIELDS:
        if not isinstance(data[field], list):
            raise ValueError(
                f"AI JSON field '{field}' must be a list."
            )

    return data