# 🚀 Deploying PawCare AI

PawCare has two deployable parts:

- **Backend** (FastAPI) → **Render**
- **Frontend** (React/Vite) → **Vercel**

Deploy the **backend first**, then point the frontend at its URL.

> **Current live deployment**
> - Frontend (Vercel): https://pawcare-ai-psi.vercel.app
> - Backend (Render): https://pawcare-ai-archana-bht2.onrender.com
>
> ⚠️ Render/Vercel subdomains are **globally unique**, so if a name is taken you'll get a
> random suffix (e.g. `-bht2`, `-psi`). Always use the exact URL shown in your dashboard.

---

## Prerequisites

- The repository pushed to GitHub: `https://github.com/ArchanaShaji1311/pawcare-ai`
- A free **Google Gemini API key** - <https://aistudio.google.com/app/apikey>
- A free **Render** account - <https://render.com>
- A free **Vercel** account - <https://vercel.com>

---

## 1️⃣ Backend → Render

### Option A - Blueprint (uses the included `render.yaml`)

1. Go to <https://dashboard.render.com> → **New** → **Blueprint**.
2. Connect your GitHub and select the **`pawcare-ai`** repo.
3. Render reads `render.yaml` and proposes a web service named **pawcare-ai-archana** (it may add a random suffix if the name is taken).
4. When prompted, set the secret env var **`GEMINI_API_KEY`** = your key.
5. Click **Apply** / **Create**. First build takes a few minutes.

### Option B - Manual Web Service

1. **New** → **Web Service** → connect the `pawcare-ai` repo.
2. Configure:
   - **Root Directory:** `backend`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type:** Free
3. **Environment → Add Environment Variable:**
   | Key              | Value                     |
   | ---------------- | ------------------------- |
   | `GEMINI_API_KEY` | _your Google AI key_      |
   | `GEMINI_MODEL`   | `gemini-flash-latest`     |
4. **Create Web Service** and wait for the deploy to go live.

### Verify

Open `https://<your-service>.onrender.com/api/health` - you should see:

```json
{ "status": "healthy", "gemini_enabled": true, "rag_documents": 22 }
```

> 📌 **Copy the backend URL** (e.g. `https://pawcare-ai-archana-bht2.onrender.com`) - you need it next.
>
> ⏳ **Free-tier note:** Render free services spin down after ~15 min idle, so the first
> request after a pause may take ~30–60s to wake. This is normal.

---

## 2️⃣ Frontend → Vercel

1. Go to <https://vercel.com/new> and import the **`pawcare-ai`** repo.
2. Configure the project:
   - **Root Directory:** `frontend`  ← click **Edit** and select it
   - **Framework Preset:** **Vite** (auto-detected)
   - **Build Command:** `npm run build` (default)
   - **Output Directory:** `dist` (default)
3. **Environment Variables → Add:**
   | Key            | Value                                   |
   | -------------- | --------------------------------------- |
   | `VITE_API_URL` | `https://pawcare-ai-archana-bht2.onrender.com` |
   (Use **your** Render URL from step 1 - **no trailing slash**.)
   > ⚠️ Vite bakes env vars at **build time** - after changing `VITE_API_URL` you MUST
   > **redeploy** on Vercel (Deployments → ⋯ → Redeploy) for it to take effect.
4. Click **Deploy**. When it finishes, open the Vercel URL 🎉

> CORS is already configured in the backend to allow any `*.vercel.app` origin, so the
> deployed frontend can call the API out of the box. If you later add a **custom domain**,
> append it to `CORS_ORIGINS` in Render.

---

## 3️⃣ Post-deploy checklist

- [ ] `GET /api/health` on Render returns `gemini_enabled: true`, `rag_documents: 22`
- [ ] Vercel site loads and the boot skeleton appears briefly
- [ ] Upload a dog photo → results show the **"Gemini Vision"** badge (not "Offline mode")
- [ ] The care plan and the "Evidence grounded…" note appear

---

## 🔄 Continuous deployment

Both platforms auto-deploy on every push to `main`:

- Push backend changes → Render rebuilds `pawcare-ai-archana`.
- Push frontend changes → Vercel rebuilds the site.

## 🧠 Updating the RAG knowledge base

If you edit `backend/app/data/knowledge_base.py`, regenerate the embedding index and commit it:

```bash
cd backend && source .venv/bin/activate
python scripts/build_kb_embeddings.py     # rewrites app/data/kb_embeddings.json
git add app/data/knowledge_base.py app/data/kb_embeddings.json
git commit -m "chore: update RAG knowledge base" && git push
```

## 🛠️ Troubleshooting

| Symptom                                   | Fix                                                                 |
| ----------------------------------------- | ------------------------------------------------------------------- |
| Frontend shows "Offline mode"             | `GEMINI_API_KEY` missing/invalid on Render, or quota hit.           |
| Network / CORS errors in the browser      | `VITE_API_URL` wrong, or backend still waking (Render cold start).  |
| First request very slow                   | Render free-tier cold start - retry after it wakes.                 |
| `rag_documents: 0` in health              | `kb_embeddings.json` missing - run the build script and redeploy.   |
