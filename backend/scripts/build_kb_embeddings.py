import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from google import genai

from app.data.knowledge_base import KB_ENTRIES

EMBED_MODEL = "gemini-embedding-001"
OUT_PATH = Path(__file__).resolve().parent.parent / "app" / "data" / "kb_embeddings.json"


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        env = Path(__file__).resolve().parent.parent / ".env"
        if env.exists():
            for line in env.read_text().splitlines():
                if line.startswith("GEMINI_API_KEY="):
                    api_key = line.split("=", 1)[1].strip()
    if not api_key:
        raise SystemExit("GEMINI_API_KEY not set")

    client = genai.Client(api_key=api_key)
    vectors: dict[str, list[float]] = {}
    for entry in KB_ENTRIES:
        text = f"{entry['title']}. {entry['text']}"
        result = client.models.embed_content(model=EMBED_MODEL, contents=[text])
        vectors[entry["id"]] = list(result.embeddings[0].values)
        print(f"embedded {entry['id']}")

    OUT_PATH.write_text(json.dumps(vectors))
    print(f"wrote {len(vectors)} vectors to {OUT_PATH}")


if __name__ == "__main__":
    main()
