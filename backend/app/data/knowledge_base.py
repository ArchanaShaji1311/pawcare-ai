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
    {
        "id": "ear-infection",
        "category": "skin_infection",
        "title": "Ear infections (otitis)",
        "text": (
            "Ear infections show as head shaking, scratching at ears, redness, odor, and "
            "brown or yellow discharge. They are common in floppy-eared breeds and often "
            "linked to allergies or moisture. A vet should examine the ear canal and "
            "prescribe cleaning plus medicated drops; never insert cotton swabs deep."
        ),
    },
    {
        "id": "hot-spots",
        "category": "skin_infection",
        "title": "Hot spots (acute moist dermatitis)",
        "text": (
            "Hot spots are red, moist, painful patches that appear suddenly and spread as "
            "the dog licks or chews. Clip surrounding fur, keep it clean and dry, prevent "
            "licking, and see a vet; they often need topical or oral treatment and an "
            "underlying-cause check (fleas, allergies)."
        ),
    },
    {
        "id": "mange-mites",
        "category": "skin_infection",
        "title": "Mange and mites",
        "text": (
            "Mange from mites causes intense itching, hair loss, crusting, and thickened "
            "skin. Sarcoptic mange is contagious; demodectic mange links to immune status. "
            "Diagnosis needs a vet skin scrape; treatment is vet-prescribed and should not "
            "be attempted with home remedies."
        ),
    },
    {
        "id": "ringworm",
        "category": "skin_infection",
        "title": "Ringworm (dermatophytosis)",
        "text": (
            "Ringworm is a fungal infection, not a worm, causing circular areas of hair "
            "loss with scaly, crusty skin. It is contagious to other pets and people. A vet "
            "confirms it and prescribes antifungal treatment; disinfect bedding and wash "
            "hands after handling."
        ),
    },
    {
        "id": "dental-disease",
        "category": "medical",
        "title": "Dental disease",
        "text": (
            "Bad breath, tartar, red or bleeding gums, and difficulty eating signal dental "
            "disease, which affects most adult dogs. It can seed infection to the heart and "
            "kidneys. Brush teeth regularly, offer dental chews, and schedule professional "
            "cleanings."
        ),
    },
    {
        "id": "eye-problems",
        "category": "medical",
        "title": "Eye irritation and infection",
        "text": (
            "Redness, squinting, discharge, cloudiness, or pawing at the eye can indicate "
            "conjunctivitis, injury, dry eye, or ulcers. Eyes are delicate - do not use "
            "human eye drops. Persistent or painful eye signs need prompt veterinary care."
        ),
    },
    {
        "id": "gi-upset",
        "category": "medical",
        "title": "Vomiting and diarrhea",
        "text": (
            "Occasional mild vomiting or diarrhea can come from diet changes or dietary "
            "indiscretion. Withhold food briefly, offer water, then a bland diet. Seek a "
            "vet urgently for blood, repeated episodes, lethargy, a bloated abdomen, or "
            "suspected toxin ingestion."
        ),
    },
    {
        "id": "parasites-worms",
        "category": "medical",
        "title": "Intestinal parasites and fleas",
        "text": (
            "Fleas, ticks, and intestinal worms cause itching, scooting, weight loss, and "
            "visible worms in stool. Keep year-round parasite prevention current and have "
            "stool checked at annual exams. Ticks should be removed promptly and the dog "
            "monitored for illness."
        ),
    },
    {
        "id": "obesity",
        "category": "diet",
        "title": "Weight management and obesity",
        "text": (
            "Excess weight strains joints and the heart and shortens lifespan. Measure "
            "food, limit treats to under 10 percent of calories, and increase gentle "
            "activity. You should be able to feel the ribs easily and see a waist from "
            "above."
        ),
    },
    {
        "id": "arthritis",
        "category": "medical",
        "title": "Arthritis and joint pain",
        "text": (
            "Stiffness, limping, reluctance to jump or climb stairs, and slowing down can "
            "indicate arthritis, especially in older or large-breed dogs. Keep the dog "
            "lean, provide soft bedding and low-impact exercise, and ask a vet about joint "
            "supplements or pain relief."
        ),
    },
    {
        "id": "heatstroke",
        "category": "wound",
        "title": "Heatstroke (emergency)",
        "text": (
            "Heavy panting, drooling, bright red gums, weakness, vomiting, or collapse in "
            "heat signal heatstroke - a life-threatening emergency. Move to shade, offer "
            "cool (not ice-cold) water, wet the body, and go to a vet immediately. Never "
            "leave a dog in a parked car."
        ),
    },
    {
        "id": "toxic-foods",
        "category": "medical",
        "title": "Toxic foods and poisoning",
        "text": (
            "Chocolate, xylitol, grapes, raisins, onions, garlic, macadamia nuts, alcohol, "
            "and many human medications are toxic to dogs. Signs include vomiting, tremors, "
            "and collapse. If ingestion is suspected, contact a vet or pet poison hotline "
            "immediately - do not wait for symptoms."
        ),
    },
    {
        "id": "paw-nail-care",
        "category": "medical",
        "title": "Paw and nail care",
        "text": (
            "Cracked pads, limping, licking paws, or overgrown nails cause discomfort. "
            "Trim nails regularly, check pads for cuts or foreign objects, and protect paws "
            "from hot pavement and ice. Excessive paw licking often points to allergies."
        ),
    },
    {
        "id": "vaccination",
        "category": "medical",
        "title": "Vaccination and preventive schedule",
        "text": (
            "Core vaccines (rabies, distemper, parvovirus, adenovirus) protect against "
            "serious disease; puppies need a series, then boosters. Keep parasite "
            "prevention and annual exams current. Ask a vet about lifestyle-based vaccines "
            "like leptospirosis or Bordetella."
        ),
    },
    {
        "id": "puppy-care",
        "category": "diet",
        "title": "Puppy life-stage care",
        "text": (
            "Puppies need a growth-formula diet, frequent small meals, socialization, and a "
            "vaccination and deworming series. Large-breed puppies need controlled growth "
            "to protect developing joints. Avoid strenuous forced exercise while joints "
            "mature."
        ),
    },
    {
        "id": "senior-care",
        "category": "medical",
        "title": "Senior dog care",
        "text": (
            "Older dogs benefit from twice-yearly checkups, joint support, dental care, and "
            "diets adjusted for lower activity. Watch for changes in weight, thirst, "
            "urination, lumps, vision, and mobility, and report them early."
        ),
    },
    {
        "id": "wound-cleaning",
        "category": "wound",
        "title": "Safe wound cleaning at home",
        "text": (
            "For minor scrapes, rinse with saline or clean water, gently pat dry, and "
            "prevent licking with an e-collar. Avoid hydrogen peroxide and alcohol, which "
            "damage tissue. Watch for swelling, pus, warmth, or odor that signal infection "
            "needing a vet."
        ),
    },
    {
        "id": "insect-bites",
        "category": "wound",
        "title": "Insect bites and stings",
        "text": (
            "Bee stings and insect bites can cause localized swelling, redness, and "
            "itching. Watch for facial swelling, hives, difficulty breathing, or collapse, "
            "which indicate an allergic reaction and need emergency care. A cool compress "
            "can ease mild local swelling."
        ),
    },
    {
        "id": "lumps-bumps",
        "category": "other",
        "title": "Skin lumps and bumps",
        "text": (
            "New lumps can be harmless (fatty masses, cysts) or serious. Note size, growth "
            "rate, firmness, and any discharge. Any rapidly growing, ulcerated, or firmly "
            "attached lump should be examined and possibly sampled by a vet."
        ),
    },
    {
        "id": "anxiety-noise",
        "category": "behavioral",
        "title": "Noise phobia and fear",
        "text": (
            "Trembling, hiding, pacing, or destructive behavior during storms or fireworks "
            "reflect noise phobia. Provide a safe den, background sound, and calm "
            "reassurance; desensitization training and, in severe cases, vet-prescribed "
            "support can help."
        ),
    },
    {
        "id": "breed-boxer",
        "category": "breed",
        "breed": "boxer",
        "title": "Boxer health profile",
        "text": (
            "Boxers are prone to certain cancers, heart conditions (cardiomyopathy), and "
            "heat sensitivity due to their short snout. Provide regular veterinary "
            "screening, avoid overheating, and keep a lean, muscular condition."
        ),
    },
    {
        "id": "breed-husky",
        "category": "breed",
        "breed": "siberian husky",
        "title": "Siberian Husky health profile",
        "text": (
            "Huskies are high-energy and prone to eye conditions (cataracts, corneal "
            "dystrophy) and zinc-responsive skin issues. They need substantial daily "
            "exercise and secure fencing, as they are escape artists and love to run."
        ),
    },
    {
        "id": "breed-pug",
        "category": "breed",
        "breed": "pug",
        "title": "Pug health profile",
        "text": (
            "Pugs are brachycephalic with breathing difficulty, eye problems, and skin "
            "fold dermatitis. Keep facial folds clean and dry, avoid heat and "
            "overexertion, and manage weight carefully to protect breathing."
        ),
    },
    {
        "id": "breed-chihuahua",
        "category": "breed",
        "breed": "chihuahua",
        "title": "Chihuahua health profile",
        "text": (
            "Chihuahuas are prone to dental disease, patellar luxation, tracheal collapse, "
            "and low blood sugar in small puppies. Support dental care, use a harness, and "
            "protect them from injury due to their small size."
        ),
    },
    {
        "id": "breed-shih-tzu",
        "category": "breed",
        "breed": "shih tzu",
        "title": "Shih Tzu health profile",
        "text": (
            "Shih Tzus are brachycephalic and prone to eye problems, skin fold and ear "
            "issues, and dental crowding. Keep facial hair trimmed away from the eyes, "
            "clean folds and ears, and avoid overheating."
        ),
    },
    {
        "id": "breed-doberman",
        "category": "breed",
        "breed": "doberman",
        "title": "Doberman health profile",
        "text": (
            "Dobermans are predisposed to dilated cardiomyopathy, von Willebrand clotting "
            "disorder, and hip dysplasia. Regular cardiac screening is important; provide "
            "structured exercise and a joint-supportive diet."
        ),
    },
    {
        "id": "breed-great-dane",
        "category": "breed",
        "breed": "great dane",
        "title": "Great Dane health profile",
        "text": (
            "Great Danes are at high risk of bloat (gastric torsion) and heart and joint "
            "conditions. Feed multiple smaller meals from a raised bowl, avoid exercise "
            "right after eating, and discuss preventive gastropexy with a vet."
        ),
    },
    {
        "id": "breed-australian-shepherd",
        "category": "breed",
        "breed": "australian shepherd",
        "title": "Australian Shepherd health profile",
        "text": (
            "Australian Shepherds are highly active herding dogs prone to eye anomalies "
            "and MDR1 drug sensitivity. They need extensive daily exercise and mental work; "
            "ask a vet about MDR1 testing before certain medications."
        ),
    },
    {
        "id": "breed-corgi",
        "category": "breed",
        "breed": "corgi",
        "title": "Corgi health profile",
        "text": (
            "Corgis have long backs and short legs, raising the risk of intervertebral "
            "disc disease and obesity. Keep them lean, discourage jumping from heights, and "
            "provide regular moderate exercise."
        ),
    },
    {
        "id": "breed-shiba-inu",
        "category": "breed",
        "breed": "shiba inu",
        "title": "Shiba Inu health profile",
        "text": (
            "Shiba Inus are prone to allergies, patellar luxation, and eye conditions. They "
            "are clean and independent; maintain skin and coat health, watch for itching, "
            "and provide consistent training and exercise."
        ),
    },
    {
        "id": "breed-cavalier",
        "category": "breed",
        "breed": "cavalier king charles spaniel",
        "title": "Cavalier King Charles Spaniel health profile",
        "text": (
            "Cavaliers are strongly predisposed to mitral valve heart disease and certain "
            "neurological conditions. Regular cardiac checkups are essential; keep them "
            "lean and report coughing or exercise intolerance promptly."
        ),
    },
]
