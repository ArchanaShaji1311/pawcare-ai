import logging

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.schemas import AnalyzeResponse
from app.services.gemini_service import GeminiService
from app.services.preprocessing import ImageValidationError, preprocess_image
from app.services.recommendation_engine import (
    aggregate_confidence,
    build_recommendations,
)
from app.services.symptom_engine import (
    build_fallback_analysis,
    compute_vet_alert,
)

settings = get_settings()
logger = logging.getLogger("pawcare")

app = FastAPI(title=settings.app_name, version=settings.app_version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_gemini = (
    GeminiService(settings.gemini_api_key, settings.gemini_model)
    if settings.gemini_enabled
    else None
)

DISCLAIMER = (
    "PawCare AI provides informational guidance only and is not a substitute for "
    "professional veterinary diagnosis. When in doubt, consult a licensed vet."
)


@app.get("/")
def root():
    return {"service": settings.app_name, "version": settings.app_version, "status": "ok"}


@app.get("/api/health")
def health():
    return {"status": "healthy", "gemini_enabled": settings.gemini_enabled}


@app.post("/api/analyze", response_model=AnalyzeResponse)
async def analyze(
    image: UploadFile = File(...),
    symptoms: str | None = Form(default=None),
    breed: str | None = Form(default=None),
):
    if image.content_type is None or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image.")

    raw = await image.read()

    try:
        processed_bytes, meta = preprocess_image(
            raw, settings.max_image_mb, settings.target_image_longest_edge
        )
    except ImageValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    ai_source = "fallback"
    if _gemini is not None:
        try:
            analysis = _gemini.analyze(processed_bytes, symptoms, breed)
            ai_source = "gemini"
        except Exception as exc:
            logger.warning("Gemini analysis failed, using fallback: %s", exc)
            analysis = build_fallback_analysis(symptoms, meta["estimated_quality"])
    else:
        analysis = build_fallback_analysis(symptoms, meta["estimated_quality"])

    if not analysis.is_dog:
        raise HTTPException(
            status_code=422,
            detail="No dog detected in the image. Please upload a clear photo of your dog.",
        )

    recommendations, resolved_breed = build_recommendations(breed, analysis.conditions)
    vet_alert = compute_vet_alert(analysis.conditions, symptoms)
    overall_confidence = aggregate_confidence(analysis.conditions)

    return AnalyzeResponse(
        is_dog=analysis.is_dog,
        image_quality=analysis.image_quality or meta["estimated_quality"],
        breed=resolved_breed if breed else None,
        overall_summary=analysis.overall_summary,
        overall_confidence=overall_confidence,
        conditions=analysis.conditions,
        recommendations=recommendations,
        vet_alert=vet_alert,
        ai_source=ai_source,
        disclaimer=DISCLAIMER,
    )
