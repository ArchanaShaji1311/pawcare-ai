# 🐾 PawCare AI — Intelligent Dog Health & Care Assistant

An AI-powered platform that helps dog owners monitor their dog's health through
**image analysis**, **symptom evaluation**, and **personalized, breed-specific
care recommendations** — with built-in ethical-AI guardrails and
vet-consultation alerts.

![Tech](https://img.shields.io/badge/React-19-149eca)
![Tech](https://img.shields.io/badge/FastAPI-Python-009688)
![Tech](https://img.shields.io/badge/Gemini-Vision-orange)

## ✨ Features

- **Image analysis** — upload a dog photo; Google **Gemini Flash** vision
  screens for allergies, skin infections, wounds, and visible behavioral cues,
  with an automatic model-fallback chain that rides through transient 429/503s.
- **Symptom evaluation engine** — rule-based triage of owner-reported symptoms.
- **Breed-specific recommendation engine** — tailored diet, exercise, and
  medical guidance across 10+ breeds (with sensible defaults for mixed breeds).
- **Ethical AI guardrails** — calibrated **confidence scores**, an overall
  confidence readout, and automatic **vet-consultation alerts** (routine →
  urgent) that escalate on severe findings or emergency keywords.
- **Robust image pipeline** — validation, EXIF-orientation fix, resizing,
  auto-contrast normalization, and quality estimation (brightness/sharpness)
  for more reliable inference.
- **Graceful degradation** — works offline with a symptom-only assessment when
  no Gemini API key is configured.

## 🏗️ Architecture

```
PawCare/
├── backend/          FastAPI + Python  → Render
│   ├── main.py                    API + endpoints (/api/analyze, /api/health)
│   └── app/
│       ├── config.py              env-based settings
│       ├── schemas.py             Pydantic models (also Gemini output schema)
│       ├── data/breeds.py         breed knowledge base
│       └── services/
│           ├── preprocessing.py   Pillow image pipeline
│           ├── gemini_service.py  Gemini vision (structured JSON output)
│           ├── symptom_engine.py  symptom triage + vet-alert logic
│           └── recommendation_engine.py  breed-specific care + confidence
└── frontend/         React 19 + Vite + TS + Tailwind v4  → Vercel
    └── src/
        ├── api.ts                 typed API client
        ├── types.ts               shared API types
        └── components/            Hero, UploadPanel, ResultsView, ...
```

## 🚀 Local Development

### 1. Backend (FastAPI)

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # then paste your Gemini key into .env
uvicorn main:app --reload --port 8000
```

Get a free Gemini API key at <https://aistudio.google.com/app/apikey> and set
`GEMINI_API_KEY` in `backend/.env`. Without a key the app still runs in
symptom-only fallback mode.

### 2. Frontend (React)

```bash
cd frontend
npm install
cp .env.example .env          # VITE_API_URL=http://localhost:8000
npm run dev                   # open http://localhost:5173
```

## ☁️ Deployment

### Backend → Render
- New **Web Service** from this repo, root directory `backend`.
- Build: `pip install -r requirements.txt`
- Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Add env var `GEMINI_API_KEY`. (A `render.yaml` blueprint is included.)

### Frontend → Vercel
- New Project from this repo, root directory `frontend`.
- Framework preset **Vite** (build `npm run build`, output `dist`).
- Add env var `VITE_API_URL` = your Render backend URL.
- SPA routing handled by the included `vercel.json`.

> CORS already allows `localhost` and any `*.vercel.app` origin.

## ⚕️ Disclaimer

PawCare AI provides informational guidance only and is **not** a substitute for
professional veterinary diagnosis. Always consult a licensed veterinarian.
