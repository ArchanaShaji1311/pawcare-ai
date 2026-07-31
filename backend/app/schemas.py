from enum import Enum

from pydantic import BaseModel, Field


class Severity(str, Enum):
    none = "none"
    mild = "mild"
    moderate = "moderate"
    severe = "severe"


class DetectedCondition(BaseModel):
    name: str = Field(description="Name of the potential condition observed")
    category: str = Field(
        description="One of: allergy, skin_infection, wound, behavioral, other"
    )
    severity: Severity
    confidence: float = Field(ge=0.0, le=1.0)
    explanation: str = Field(description="What visual/described evidence supports this")


class GeminiAnalysis(BaseModel):
    is_dog: bool = Field(description="Whether the image actually contains a dog")
    image_quality: str = Field(description="One of: good, fair, poor")
    overall_summary: str
    conditions: list[DetectedCondition]


class Recommendation(BaseModel):
    title: str
    detail: str


class RecommendationSet(BaseModel):
    diet: list[Recommendation]
    exercise: list[Recommendation]
    medical: list[Recommendation]


class VetAlert(BaseModel):
    triggered: bool
    urgency: str = Field(description="One of: none, routine, soon, urgent")
    reasons: list[str]


class Source(BaseModel):
    id: str
    title: str
    snippet: str


class AnalyzeResponse(BaseModel):
    is_dog: bool
    image_quality: str
    breed: str | None = None
    overall_summary: str
    overall_confidence: float = Field(ge=0.0, le=1.0)
    conditions: list[DetectedCondition]
    recommendations: RecommendationSet
    vet_alert: VetAlert
    sources: list[Source] = []
    ai_source: str = Field(description="gemini or fallback")
    disclaimer: str


class BreedInfo(BaseModel):
    name: str
    size: str
    common_health_risks: list[str]
