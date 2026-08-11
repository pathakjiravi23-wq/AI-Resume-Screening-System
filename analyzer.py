from google.genai import Client, models, types
from config import MODEL, API_KEY
from schemas import Resume

client = Client(api_key=API_KEY)


def resume_analyzer(text: str) -> Resume:
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=text,
            config=types.GenerateContentConfig(
                response_schema=Resume,
                response_mime_type="application/json",
                max_output_tokens=2000,
                system_instruction=(
                    "You're a resume analyzer. "
                    "Extract and return only data matching the supplied schema."
                ),
            ),
        )

        parsed = response.parsed

        if isinstance(parsed, Resume):
            return parsed

        raise ValueError("Failed to parse resume into Resume schema")

    except Exception as e:
        print(f"Data extraction failed: {e}")
        raise
