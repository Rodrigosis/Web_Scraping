import logging
from logging.config import dictConfig

LOG_FORMAT: str = '%(levelprefix)s %(asctime)s - %(message)s'
LOG_LEVEL: str = 'DEBUG'

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",

        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "foo-logger": {"handlers": ["default"], "level": LOG_LEVEL},
    },
}

dictConfig(log_config)
logger = logging.getLogger('fastapi')
