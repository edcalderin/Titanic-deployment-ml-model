import logging
from typing import List

from pydantic import AnyHttpUrl, BaseSettings

PROJECT_NAME = "Titanic Prediction API"


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # Meta
    logging: LoggingSettings = LoggingSettings()

    BACKEND_CORS_ORIGINALS: List[AnyHttpUrl] = []
