from app.data.breeds import get_breed
from app.schemas import (
    DetectedCondition,
    Recommendation,
    RecommendationSet,
    Severity,
)

_MEDICAL_BY_CATEGORY: dict[str, Recommendation] = {
    "allergy": Recommendation(
        title="Allergy management",
        detail="Identify and remove triggers (food, fleas, environment). A vet may "
        "recommend antihistamines, medicated shampoo, or an elimination diet.",
    ),
    "skin_infection": Recommendation(
        title="Skin infection care",
        detail="Keep the area clean and dry. Bacterial or yeast infections usually "
        "need vet-prescribed topical or oral treatment. Avoid self-medicating.",
    ),
    "wound": Recommendation(
        title="Wound care",
        detail="Gently clean minor wounds and prevent licking. Deep, bleeding, or "
        "swelling wounds need prompt veterinary attention.",
    ),
    "behavioral": Recommendation(
        title="Behavioral support",
        detail="Rule out pain first. Maintain routine, enrichment, and positive "
        "reinforcement; a vet or behaviorist can help persistent issues.",
    ),
}

_GENERAL_MEDICAL = Recommendation(
    title="Preventive care",
    detail="Keep vaccinations, parasite prevention, and annual check-ups current. "
    "Monitor appetite, energy, and stool for early warning signs.",
)


def build_recommendations(
    breed: str | None, conditions: list[DetectedCondition]
) -> tuple[RecommendationSet, str]:
    resolved_name, data = get_breed(breed)

    diet = [Recommendation(title="", detail=d) for d in data["diet"]]
    exercise = [Recommendation(title="", detail=e) for e in data["exercise"]]

    medical: list[Recommendation] = []
    seen: set[str] = set()
    for condition in conditions:
        rec = _MEDICAL_BY_CATEGORY.get(condition.category)
        if rec and rec.title not in seen:
            medical.append(rec)
            seen.add(rec.title)
    medical.append(_GENERAL_MEDICAL)

    risks = ", ".join(data["common_health_risks"])
    medical.insert(
        0,
        Recommendation(
            title=f"{resolved_name} health watch",
            detail=f"Common risks for this breed: {risks}. "
            "Ask your vet about breed-specific screening.",
        ),
    )

    return RecommendationSet(diet=diet, exercise=exercise, medical=medical), resolved_name


def aggregate_confidence(conditions: list[DetectedCondition]) -> float:
    if not conditions:
        return 0.9
    weights = {
        Severity.severe: 1.0,
        Severity.moderate: 0.7,
        Severity.mild: 0.4,
        Severity.none: 0.1,
    }
    total_weight = sum(weights[c.severity] for c in conditions)
    if total_weight == 0:
        return round(sum(c.confidence for c in conditions) / len(conditions), 2)
    weighted = sum(c.confidence * weights[c.severity] for c in conditions)
    return round(weighted / total_weight, 2)
