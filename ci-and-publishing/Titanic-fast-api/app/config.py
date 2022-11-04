import logging
import sys
from types import FrameType
from typing import List, cast

from loguru import logger
from pydantic import AnyHttpUrl, BaseSettings


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    PROJECT_NAME: str = "Titanic Prediction API"

    # Meta
    logging: LoggingSettings = LoggingSettings()

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "https://localhost:3000",
        "https://localhost:8000",
    ]

    class Config:
        case_sensitive = True


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists.
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_and_logging(config: Settings):
    logging.basicConfig(
        handlers=[InterceptHandler(level=config.logging.LOGGING_LEVEL)],
        level=config.logging.LOGGING_LEVEL,
        force=True,
    )


settings = Settings()
