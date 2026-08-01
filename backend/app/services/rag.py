import json
import math
from pathlib import Path

from google import genai
from google.genai import types

from app.data.knowledge_base import KB_ENTRIES

EMBED_MODEL = "gemini-embedding-001"
_EMB_PATH = Path(__file__).resolve().parent.parent / "data" / "kb_embeddings.json"


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


class RagRetriever:
    def __init__(self, api_key: str | None):
        self._client = (
            genai.Client(
                api_key=api_key,
                http_options=types.HttpOptions(
                    timeout=8000,
                    retry_options=types.HttpRetryOptions(attempts=1),
                ),
            )
            if api_key
            else None
        )
        self._entries = {e["id"]: e for e in KB_ENTRIES}
        self._vectors = self._load_vectors()

    @property
    def vector_count(self) -> int:
        return len(self._vectors)

    def _load_vectors(self) -> dict[str, list[float]]:
        if _EMB_PATH.exists():
            try:
                return json.loads(_EMB_PATH.read_text())
            except Exception:
                return {}
        return {}

    def _embed(self, text: str) -> list[float] | None:
        if not self._client:
            return None
        try:
            result = self._client.models.embed_content(
                model=EMBED_MODEL, contents=[text]
            )
            return list(result.embeddings[0].values)
        except Exception:
            return None

    def retrieve(self, query: str, breed: str | None = None, k: int = 4) -> list[dict]:
        tokens = {t for t in query.lower().split() if len(t) > 2}
        keyword = {
            cid: self._keyword_score(entry, tokens, breed)
            for cid, entry in self._entries.items()
        }

        query_vector = self._embed(query) if self._vectors else None
        if query_vector:
            embedding = _normalize(
                {cid: _cosine(query_vector, vec) for cid, vec in self._vectors.items()}
            )
            keyword_norm = _normalize(keyword)
            blended = {
                cid: 0.7 * embedding.get(cid, 0.0) + 0.3 * keyword_norm.get(cid, 0.0)
                for cid in self._entries
            }
        else:
            blended = keyword

        ranked = sorted(blended.items(), key=lambda item: item[1], reverse=True)
        results = [self._entries[cid] for cid, _ in ranked[:k]]
        return _ensure_breed(results, breed, self._entries)

    @staticmethod
    def _keyword_score(entry: dict, tokens: set[str], breed: str | None) -> float:
        text = f"{entry['title']} {entry['text']}".lower()
        score = float(sum(1 for t in tokens if t in text))
        if breed and entry.get("breed") == breed.strip().lower():
            score += 5.0
        return score


def _normalize(scores: dict[str, float]) -> dict[str, float]:
    if not scores:
        return {}
    lo = min(scores.values())
    hi = max(scores.values())
    if hi - lo < 1e-9:
        return {cid: 0.0 for cid in scores}
    return {cid: (v - lo) / (hi - lo) for cid, v in scores.items()}


def _ensure_breed(
    results: list[dict], breed: str | None, entries: dict[str, dict]
) -> list[dict]:
    if not breed:
        return results
    key = breed.strip().lower()
    breed_entry = next(
        (e for e in entries.values() if e.get("breed") == key), None
    )
    if breed_entry and breed_entry not in results:
        results = [breed_entry] + results[:-1] if results else [breed_entry]
    return results
