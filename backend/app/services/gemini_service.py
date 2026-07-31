from google import genai
from google.genai import types

from app.schemas import VisionAnalysis
from app.services.prompts import build_context

_FALLBACK_MODELS = [
    "gemini-3.5-flash",
    "gemini-flash-lite-latest",
    "gemini-3.1-flash-lite",
    "gemini-2.0-flash",
]

_TRANSIENT_CODES = ("429", "500", "502", "503", "UNAVAILABLE", "RESOURCE_EXHAUSTED")


class GeminiService:
    def __init__(self, api_key: str, model: str):
        self._client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(
                timeout=12000,
                retry_options=types.HttpRetryOptions(attempts=1),
            ),
        )
        self._models = [model] + [m for m in _FALLBACK_MODELS if m != model]

    def analyze(
        self,
        image_bytes: str | bytes,
        symptoms: str | None,
        breed: str | None,
        grounding: str | None = None,
    ) -> VisionAnalysis:
        contents = [
            types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
            build_context(grounding, breed, symptoms),
        ]
        config = types.GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json",
            response_schema=VisionAnalysis,
        )

        last_error: Exception | None = None
        for model in self._models:
            try:
                response = self._client.models.generate_content(
                    model=model, contents=contents, config=config
                )
                parsed = response.parsed
                if isinstance(parsed, VisionAnalysis):
                    return parsed
                return VisionAnalysis.model_validate_json(response.text)
            except Exception as exc:
                last_error = exc
                if not any(code in str(exc) for code in _TRANSIENT_CODES):
                    raise
        raise last_error if last_error else RuntimeError("Gemini analysis failed")
