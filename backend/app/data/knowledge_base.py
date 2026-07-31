KB_ENTRIES: list[dict] = [
    {
        "id": "allergy-overview",
        "category": "allergy",
        "title": "Canine allergies: signs and triggers",
        "text": (
            "Allergies in dogs commonly show as itching, redness, recurrent ear "
            "infections, hair loss, and licking or chewing of paws. Triggers include "
            "fleas, food proteins, pollens, dust mites, and mold. Persistent scratching "
            "or hot spots warrant a vet visit; a vet may advise antihistamines, "
            "medicated shampoo, flea control, or an 8-12 week elimination diet."
        ),
    },
    {
        "id": "allergy-food",
        "category": "allergy",
        "title": "Food allergy management",
        "text": (
            "Food allergies often cause year-round itching and gastrointestinal upset. "
            "The gold standard for diagnosis is a strict elimination diet using a novel "
            "or hydrolyzed protein for 8-12 weeks with no other foods or treats. "
            "Reintroduce ingredients one at a time to identify the trigger."
        ),
    },
    {
        "id": "skin-infection-pyoderma",
        "category": "skin_infection",
        "title": "Bacterial skin infection (pyoderma)",
        "text": (
            "Pyoderma presents as pustules, crusting, redness, odor, and circular "
            "scaling. It is frequently secondary to allergies or moisture trapped in "
            "skin folds. Keep the area clean and dry. Bacterial infections usually need "
            "vet-prescribed topical or oral antibiotics; avoid self-medicating."
        ),
    },
    {
        "id": "skin-infection-yeast",
        "category": "skin_infection",
        "title": "Yeast dermatitis",
        "text": (
            "Yeast (Malassezia) overgrowth causes greasy, red, itchy skin with a musty "
            "odor, often in ears, paws, and skin folds. It thrives in warm, moist areas "
            "and often accompanies allergies. Antifungal shampoos and vet-prescribed "
            "treatment help; address the underlying allergy to prevent recurrence."
        ),
    },
    {
        "id": "wound-minor",
        "category": "wound",
        "title": "Caring for minor wounds",
        "text": (
            "For small, shallow wounds, gently clean with saline or dilute antiseptic, "
            "trim surrounding fur, and prevent licking with an e-collar. Monitor for "
            "swelling, discharge, or odor. Do not use hydrogen peroxide repeatedly as it "
            "delays healing."
        ),
    },
    {
        "id": "wound-emergency",
        "category": "wound",
        "title": "Wounds that need urgent veterinary care",
        "text": (
            "Seek immediate veterinary care for deep or gaping wounds, heavy or "
            "non-stop bleeding, bites, wounds over the chest or abdomen, embedded "
            "objects, or any wound with significant swelling, pus, or fever. Apply gentle "
            "pressure with a clean cloth to control bleeding on the way to the clinic."
        ),
    },
    {
        "id": "behavior-pain",
        "category": "behavioral",
        "title": "Behavior changes can signal pain",
        "text": (
            "Sudden aggression, hiding, restlessness, reduced appetite, or lethargy can "
            "indicate pain or illness rather than a training issue. Rule out medical "
            "causes with a vet first. Maintain routine, enrichment, and positive "
            "reinforcement; a veterinary behaviorist can help persistent problems."
        ),
    },
    {
        "id": "behavior-anxiety",
        "category": "behavioral",
        "title": "Anxiety and stress signals",
        "text": (
            "Pacing, panting, whining, destructive chewing, and excessive licking can "
            "reflect anxiety. Provide predictable routines, safe spaces, exercise, and "
            "gradual desensitization. Severe separation anxiety may need a behavior plan "
            "and, in some cases, vet-prescribed support."
        ),
    },
    {
        "id": "care-diet-general",
        "category": "diet",
        "title": "General canine nutrition",
        "text": (
            "Feed a complete, balanced diet appropriate for life stage and size. Measure "
            "portions to prevent obesity, keep treats under 10 percent of daily calories, "
            "and ensure constant fresh water. Omega-3 fatty acids support skin and coat "
            "health and can help manage allergies."
        ),
    },
    {
        "id": "care-exercise-general",
        "category": "exercise",
        "title": "Exercise fundamentals",
        "text": (
            "Most dogs need 30-90 minutes of daily activity depending on breed, age, and "
            "health. Combine walks with play and training for physical and mental "
            "stimulation. Avoid intense exercise in heat, and protect brachycephalic "
            "breeds from overexertion and breathing stress."
        ),
    },
    {
        "id": "care-preventive",
        "category": "medical",
        "title": "Preventive care essentials",
        "text": (
            "Keep vaccinations, parasite prevention, and dental care up to date, and "
            "schedule annual wellness exams. Monitor appetite, energy, weight, and stool "
            "for early warning signs. Early detection greatly improves outcomes."
        ),
    },
    {
        "id": "ethics-confidence",
        "category": "medical",
        "title": "Limits of AI screening",
        "text": (
            "AI photo screening can flag possible concerns but cannot diagnose. Findings "
            "carry uncertainty and depend on image quality and visible evidence. Low "
            "confidence, severe signs, or emergency symptoms should always prompt a "
            "veterinary consultation. This tool supports, never replaces, a licensed vet."
        ),
    },
    {
        "id": "breed-labrador",
        "category": "breed",
        "breed": "labrador retriever",
        "title": "Labrador Retriever health profile",
        "text": (
            "Labradors are prone to obesity, hip and elbow dysplasia, ear infections, and "
            "allergies. Use measured portions and a large-breed formula with joint "
            "support. Swimming is excellent low-impact exercise; dry ears after swimming."
        ),
    },
    {
        "id": "breed-german-shepherd",
        "category": "breed",
        "breed": "german shepherd",
        "title": "German Shepherd health profile",
        "text": (
            "German Shepherds are predisposed to hip and elbow dysplasia, degenerative "
            "myelopathy, bloat, and allergies. Split meals to reduce bloat risk, avoid "
            "hard exercise right after eating, and provide structured mental work."
        ),
    },
    {
        "id": "breed-golden-retriever",
        "category": "breed",
        "breed": "golden retriever",
        "title": "Golden Retriever health profile",
        "text": (
            "Golden Retrievers have a higher cancer predisposition and are prone to hip "
            "dysplasia, skin allergies, and ear infections. Control calories, use "
            "antioxidant-rich food and omega fatty acids, and dry ears after swimming."
        ),
    },
    {
        "id": "breed-french-bulldog",
        "category": "breed",
        "breed": "french bulldog",
        "title": "French Bulldog health profile",
        "text": (
            "French Bulldogs are brachycephalic and prone to breathing difficulty, skin "
            "fold dermatitis, allergies, and spinal issues. Avoid heat and overexertion, "
            "keep facial folds clean and dry, and manage weight carefully."
        ),
    },
    {
        "id": "breed-bulldog",
        "category": "breed",
        "breed": "bulldog",
        "title": "Bulldog health profile",
        "text": (
            "Bulldogs are brachycephalic with risks of airway problems, skin fold "
            "dermatitis, and hip dysplasia. Exercise lightly in cool conditions, keep "
            "folds clean, and maintain a lean body weight."
        ),
    },
    {
        "id": "breed-poodle",
        "category": "breed",
        "breed": "poodle",
        "title": "Poodle health profile",
        "text": (
            "Poodles are prone to allergies, ear infections, sebaceous adenitis, and hip "
            "dysplasia. Regular grooming keeps skin healthy; watch for food sensitivities "
            "and provide daily activity plus mental challenges."
        ),
    },
    {
        "id": "breed-beagle",
        "category": "breed",
        "breed": "beagle",
        "title": "Beagle health profile",
        "text": (
            "Beagles are food-motivated and prone to obesity, ear infections, allergies, "
            "and epilepsy. Measure food strictly, avoid table scraps, and exercise in "
            "secure areas since they follow scents."
        ),
    },
    {
        "id": "breed-dachshund",
        "category": "breed",
        "breed": "dachshund",
        "title": "Dachshund health profile",
        "text": (
            "Dachshunds are at high risk of intervertebral disc disease due to their long "
            "spine, plus obesity and skin allergies. Keep them lean, avoid stairs and "
            "jumping, and use ramps to protect the back."
        ),
    },
    {
        "id": "breed-rottweiler",
        "category": "breed",
        "breed": "rottweiler",
        "title": "Rottweiler health profile",
        "text": (
            "Rottweilers are prone to hip and elbow dysplasia, obesity, and certain heart "
            "conditions. Feed a large-breed formula with joint support, control calories, "
            "and provide structured strength and obedience exercise."
        ),
    },
    {
        "id": "breed-yorkshire-terrier",
        "category": "breed",
        "breed": "yorkshire terrier",
        "title": "Yorkshire Terrier health profile",
        "text": (
            "Yorkshire Terriers are prone to dental disease, tracheal collapse, and skin "
            "allergies. Support dental health, feed small frequent meals, and use a "
            "harness instead of a collar to protect the trachea."
        ),
    },
]
