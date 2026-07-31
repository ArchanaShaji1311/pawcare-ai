import base64

from openai import OpenAI

from app.schemas import VisionAnalysis
from app.services.prompts import JSON_SHAPE_INSTRUCTION, build_context


class OpenAIService:
    def __init__(self, api_key: str, model: str):
        self._client = OpenAI(api_key=api_key, timeout=15.0, max_retries=0)
        self._model = model

    def analyze(
        self,
        image_bytes: str | bytes,
        symptoms: str | None,
        breed: str | None,
        grounding: str | None = None,
    ) -> VisionAnalysis:
        if isinstance(image_bytes, str):
            image_bytes = image_bytes.encode()
        b64 = base64.b64encode(image_bytes).decode()
        context = build_context(grounding, breed, symptoms)

        response = self._client.chat.completions.create(
            model=self._model,
            temperature=0.2,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": context + "\n\n" + JSON_SHAPE_INSTRUCTION},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analyze this dog photo and return the JSON object.",
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
                        },
                    ],
                },
            ],
        )
        content = response.choices[0].message.content or "{}"
        return VisionAnalysis.model_validate_json(content)
