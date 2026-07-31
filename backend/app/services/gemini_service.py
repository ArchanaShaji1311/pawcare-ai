from google import genai
from google.genai import types

from app.schemas import GeminiAnalysis

_SYSTEM_PROMPT = """You are PawCare AI, a veterinary triage assistant analyzing a dog photo.
You are NOT a substitute for a licensed veterinarian.

Examine the image (and any owner-reported symptoms) for visible signs of:
- allergies (redness, rashes, hot spots, hair loss, inflamed skin)
- skin infections (pustules, crusting, discharge, scaling, odor cues)
- wounds (cuts, abrasions, swelling, bleeding, foreign objects)
- behavioral / posture issues visible in the image (guarding, distress)

Rules:
- If the image is not clearly a dog, set is_dog=false and return no conditions.
- Assign a calibrated confidence (0-1). Be conservative; low confidence when unsure.
- Only report conditions with visible or clearly described evidence.
- category MUST be one of: allergy, skin_infection, wound, behavioral, other.
- severity MUST be one of: none, mild, moderate, severe.
- Keep explanations short, specific, and evidence-based.
Return ONLY structured data matching the schema."""


_FALLBACK_MODELS = [
    "gemini-3.5-flash",
    "gemini-flash-lite-latest",
    "gemini-3.1-flash-lite",
    "gemini-2.0-flash",
]

_TRANSIENT_CODES = ("429", "500", "502", "503", "UNAVAILABLE", "RESOURCE_EXHAUSTED")


class GeminiService:
    def __init__(self, api_key: str, model: str):
        self._client = genai.Client(api_key=api_key)
        self._models = [model] + [m for m in _FALLBACK_MODELS if m != model]

    def analyze(
        self,
        image_bytes: str | bytes,
        symptoms: str | None,
        breed: str | None,
        grounding: str | None = None,
    ) -> GeminiAnalysis:
        context_parts = [_SYSTEM_PROMPT]
        if grounding:
            context_parts.append(
                "Ground your assessment in these veterinary reference notes; "
                "prefer them over general knowledge where relevant:\n" + grounding
            )
        if breed:
            context_parts.append(f"Owner reports the breed as: {breed}.")
        if symptoms:
            context_parts.append(f"Owner-reported symptoms: {symptoms}")
        else:
            context_parts.append("No symptoms were reported by the owner.")

        contents = [
            types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
            "\n".join(context_parts),
        ]
        config = types.GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json",
            response_schema=GeminiAnalysis,
        )

        last_error: Exception | None = None
        for model in self._models:
            try:
                response = self._client.models.generate_content(
                    model=model, contents=contents, config=config
                )
                parsed = response.parsed
                if isinstance(parsed, GeminiAnalysis):
                    return parsed
                return GeminiAnalysis.model_validate_json(response.text)
            except Exception as exc:
                last_error = exc
                if not any(code in str(exc) for code in _TRANSIENT_CODES):
                    raise
        raise last_error if last_error else RuntimeError("Gemini analysis failed")
