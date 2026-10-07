from pydantic_settings import SettingsConfigDict
import logging

from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev FastAPI example application"

    logging_level: int = logging.DEBUG

    model_config = SettingsConfigDict(env_file=".env")
