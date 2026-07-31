from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    gemini_api_key: str = ""
    gemini_model: str = "gemini-flash-latest"

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"

    llm_provider: str = "auto"

    cors_origins: str = (
        "http://localhost:5173,"
        "http://127.0.0.1:5173,"
        "http://localhost:4173"
    )

    app_name: str = "PawCare AI"
    app_version: str = "1.0.0"

    max_image_mb: int = 10
    target_image_longest_edge: int = 768

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    @property
    def active_provider(self) -> str:
        choice = self.llm_provider.strip().lower()
        if choice == "gemini":
            return "gemini" if self.gemini_api_key.strip() else "none"
        if choice == "openai":
            return "openai" if self.openai_api_key.strip() else "none"
        if self.gemini_api_key.strip():
            return "gemini"
        if self.openai_api_key.strip():
            return "openai"
        return "none"

    @property
    def ai_enabled(self) -> bool:
        return self.active_provider != "none"

    @property
    def gemini_enabled(self) -> bool:
        return bool(self.gemini_api_key.strip())


@lru_cache
def get_settings() -> Settings:
    return Settings()
