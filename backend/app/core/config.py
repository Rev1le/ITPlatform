from pydantic import BaseSettings


class Settings(BaseSettings):
    EDGEDB_DSN: str | None = None


settings = Settings()
