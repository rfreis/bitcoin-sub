import os
import logging.config
from pathlib import Path


# Logging
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
LOG_DIR = BASE_DIR.joinpath("log")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",  # noqa
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "verbose",
        },
        "app": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR.joinpath("app.log"),
            "maxBytes": 1024 * 1024 * 100,  # 100MB
            "backupCount": 10,
            "formatter": "verbose",
        },
        "messages": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR.joinpath("messages.log"),
            "maxBytes": 1024 * 1024 * 100,  # 100MB
            "backupCount": 10,
            "formatter": "simple",
        },
    },
    "loggers": {
        "app": {
            "handlers": ["app", "console"],
            "propagate": True,
            "level": "DEBUG",
        },
        "subscriber": {
            "handlers": ["app", "console"],
            "propagate": True,
            "level": "DEBUG",
        },
        "messages": {
            "handlers": ["messages"],
            "propagate": False,
            "level": "DEBUG",
        },
    },
}

logging.config.dictConfig(LOGGING)


# General settings
PUB_BROKER_URL = os.environ.get("PUB_BROKER_URL")
HASHBLOCK_TASK_NAME = os.environ.get("HASHBLOCK_TASK_NAME")
HASHBLOCK_ZMQ_PORT = os.environ.get("HASHBLOCK_ZMQ_PORT")
