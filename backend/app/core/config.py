from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    EDGEDB_DSN: str | None = None


settings = Settings()
