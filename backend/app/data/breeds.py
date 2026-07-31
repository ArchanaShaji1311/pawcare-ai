BREEDS: dict[str, dict] = {
    "labrador retriever": {
        "size": "large",
        "common_health_risks": ["hip dysplasia", "obesity", "ear infections", "allergies"],
        "diet": [
            "Measured portions twice daily; Labradors are prone to obesity.",
            "Choose large-breed formula with glucosamine for joint support.",
            "Limit high-fat treats to under 10% of daily calories.",
        ],
        "exercise": [
            "At least 60 minutes of active exercise daily.",
            "Swimming is excellent and low-impact for their joints.",
            "Include retrieval games for mental stimulation.",
        ],
    },
    "german shepherd": {
        "size": "large",
        "common_health_risks": ["hip/elbow dysplasia", "degenerative myelopathy", "bloat", "allergies"],
        "diet": [
            "Split meals into two servings to reduce bloat risk.",
            "High-quality protein supports muscle maintenance.",
            "Add omega-3s for coat and joint health.",
        ],
        "exercise": [
            "Needs 90+ minutes of exercise and mental work daily.",
            "Structured training and scent work prevent boredom.",
            "Avoid intense exercise right after meals (bloat risk).",
        ],
    },
    "golden retriever": {
        "size": "large",
        "common_health_risks": ["cancer predisposition", "hip dysplasia", "skin allergies", "ear infections"],
        "diet": [
            "Controlled calories; goldens gain weight easily.",
            "Antioxidant-rich food supports long-term health.",
            "Omega fatty acids help manage skin allergies.",
        ],
        "exercise": [
            "60-90 minutes daily, they love fetch and water.",
            "Social play helps this friendly breed thrive.",
            "Dry ears thoroughly after swimming.",
        ],
    },
    "french bulldog": {
        "size": "small",
        "common_health_risks": ["brachycephalic airway syndrome", "skin fold dermatitis", "allergies", "spinal issues"],
        "diet": [
            "Portion carefully; low activity means easy weight gain.",
            "Limited-ingredient diets help with common food allergies.",
            "Elevated bowls can ease breathing while eating.",
        ],
        "exercise": [
            "Short, gentle walks; avoid heat and overexertion.",
            "Never exercise hard in hot/humid weather (breathing risk).",
            "Clean facial skin folds regularly to prevent infection.",
        ],
    },
    "bulldog": {
        "size": "medium",
        "common_health_risks": ["brachycephalic airway syndrome", "skin fold dermatitis", "hip dysplasia"],
        "diet": [
            "Strict portion control to avoid obesity.",
            "Skin-supporting nutrients for fold-prone skin.",
        ],
        "exercise": [
            "Light activity in cool conditions only.",
            "Keep sessions short to protect breathing.",
        ],
    },
    "poodle": {
        "size": "medium",
        "common_health_risks": ["allergies", "ear infections", "sebaceous adenitis", "hip dysplasia"],
        "diet": [
            "Balanced diet with skin/coat supporting nutrients.",
            "Watch for grain or protein sensitivities.",
        ],
        "exercise": [
            "Active breed needing 60 minutes plus mental challenges.",
            "Regular grooming keeps skin healthy.",
        ],
    },
    "beagle": {
        "size": "medium",
        "common_health_risks": ["obesity", "ear infections", "allergies", "epilepsy"],
        "diet": [
            "Measure food strictly; beagles overeat given the chance.",
            "Avoid table scraps that drive weight gain.",
        ],
        "exercise": [
            "At least 60 minutes; scent games satisfy their nose.",
            "Secure areas only, they follow scents and roam.",
        ],
    },
    "dachshund": {
        "size": "small",
        "common_health_risks": ["intervertebral disc disease", "obesity", "skin allergies"],
        "diet": [
            "Keep lean; extra weight strains their long spine.",
            "Small, measured meals twice daily.",
        ],
        "exercise": [
            "Moderate walks; avoid stairs and jumping.",
            "Use ramps to protect the back.",
        ],
    },
    "rottweiler": {
        "size": "large",
        "common_health_risks": ["hip/elbow dysplasia", "obesity", "heart conditions"],
        "diet": [
            "Large-breed formula with joint support.",
            "Control calories to protect joints and heart.",
        ],
        "exercise": [
            "60-90 minutes of exercise and structured training.",
            "Strength and obedience work suit this breed.",
        ],
    },
    "yorkshire terrier": {
        "size": "toy",
        "common_health_risks": ["dental disease", "tracheal collapse", "skin allergies"],
        "diet": [
            "Small kibble supports dental health.",
            "Frequent small meals to maintain blood sugar.",
        ],
        "exercise": [
            "Short daily walks and indoor play.",
            "Use a harness, not a collar, to protect the trachea.",
        ],
    },
}

DEFAULT_BREED = {
    "size": "medium",
    "common_health_risks": ["allergies", "skin infections", "obesity", "ear infections"],
    "diet": [
        "Feed a complete, balanced diet appropriate for age and size.",
        "Measure portions and keep treats under 10% of daily calories.",
        "Ensure constant access to fresh water.",
    ],
    "exercise": [
        "Aim for 30-60 minutes of daily activity.",
        "Mix walks with play for physical and mental stimulation.",
        "Adjust intensity to age and health status.",
    ],
}


def get_breed(breed: str | None) -> tuple[str, dict]:
    if not breed:
        return "Unknown", DEFAULT_BREED
    key = breed.strip().lower()
    if key in BREEDS:
        return breed.strip().title(), BREEDS[key]
    for name, data in BREEDS.items():
        if key in name or name in key:
            return name.title(), data
    return breed.strip().title(), DEFAULT_BREED
