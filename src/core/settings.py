from functools import cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Настройки проекта."""

    DEBUG: bool = False
    ML_ROOT_PATH: str = ""

    class Config:
        env_file = ".env"


@cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
