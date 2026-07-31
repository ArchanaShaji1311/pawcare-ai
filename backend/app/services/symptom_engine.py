from app.schemas import (
    DetectedCondition,
    VisionAnalysis,
    Severity,
    VetAlert,
)

_KEYWORD_RULES: list[dict] = [
    {
        "category": "allergy",
        "name": "Possible allergic reaction",
        "keywords": ["itch", "scratch", "red", "rash", "hives", "lick", "hot spot", "hair loss", "bald"],
        "severity": Severity.moderate,
        "confidence": 0.55,
        "explanation": "Reported itching/redness patterns are consistent with allergies.",
    },
    {
        "category": "skin_infection",
        "name": "Possible skin infection",
        "keywords": ["pus", "crust", "smell", "odor", "oozing", "discharge", "scab", "flaky", "infection"],
        "severity": Severity.moderate,
        "confidence": 0.55,
        "explanation": "Reported discharge/crusting can indicate a skin infection.",
    },
    {
        "category": "wound",
        "name": "Possible wound or injury",
        "keywords": ["cut", "bleed", "wound", "swollen", "swelling", "limp", "injury", "bite", "gash"],
        "severity": Severity.severe,
        "confidence": 0.6,
        "explanation": "Reported bleeding/swelling suggests a wound needing attention.",
    },
    {
        "category": "behavioral",
        "name": "Behavioral / distress signs",
        "keywords": ["aggress", "anxious", "hiding", "whimper", "lethargic", "not eating", "restless", "pacing"],
        "severity": Severity.mild,
        "confidence": 0.5,
        "explanation": "Reported behavior changes may signal discomfort or stress.",
    },
]

_EMERGENCY_KEYWORDS = [
    "not breathing", "seizure", "collapse", "unconscious", "blood", "bleeding",
    "vomiting blood", "can't walk", "cannot walk", "poison", "swollen abdomen",
    "pale gums", "choking", "bloat",
]


def evaluate_symptoms(symptoms: str | None) -> list[DetectedCondition]:
    if not symptoms:
        return []
    text = symptoms.lower()
    results: list[DetectedCondition] = []
    for rule in _KEYWORD_RULES:
        if any(kw in text for kw in rule["keywords"]):
            results.append(
                DetectedCondition(
                    name=rule["name"],
                    category=rule["category"],
                    severity=rule["severity"],
                    confidence=rule["confidence"],
                    explanation=rule["explanation"],
                )
            )
    return results


def build_fallback_analysis(
    symptoms: str | None, image_quality: str
) -> VisionAnalysis:
    conditions = evaluate_symptoms(symptoms)
    if conditions:
        summary = (
            "Based on reported symptoms, the items below may warrant attention. "
            "This offline assessment does not analyze the photo; add a Gemini API "
            "key for full image analysis."
        )
    else:
        summary = (
            "No specific concerns were identified from the reported information. "
            "Add a Gemini API key to enable full AI image analysis."
        )
    return VisionAnalysis(
        is_dog=True,
        image_quality=image_quality,
        overall_summary=summary,
        conditions=conditions,
    )


def compute_vet_alert(
    conditions: list[DetectedCondition], symptoms: str | None
) -> VetAlert:
    reasons: list[str] = []
    urgency = "none"

    text = (symptoms or "").lower()
    if any(kw in text for kw in _EMERGENCY_KEYWORDS):
        return VetAlert(
            triggered=True,
            urgency="urgent",
            reasons=["Reported symptoms include potential emergency signs."],
        )

    severe = [c for c in conditions if c.severity == Severity.severe]
    moderate = [c for c in conditions if c.severity == Severity.moderate]
    low_conf = [c for c in conditions if 0 < c.confidence < 0.5]

    if severe:
        urgency = "soon"
        reasons.append("A potentially severe condition was detected.")
    elif moderate:
        urgency = "routine"
        reasons.append("A moderate condition was detected that a vet should review.")

    if low_conf:
        reasons.append(
            "Some findings have low AI confidence; a vet can confirm accurately."
        )
        if urgency == "none":
            urgency = "routine"

    return VetAlert(triggered=urgency != "none", urgency=urgency, reasons=reasons)
