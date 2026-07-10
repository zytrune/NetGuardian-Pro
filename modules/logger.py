"""
NetGuardian Pro - Central Logging System
Stores rotating application logs in the user's local application data.
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path


def _get_log_directory():
    if os.name == "nt":
        base_directory = Path(os.environ.get("LOCALAPPDATA", Path.home()))
    else:
        base_directory = Path.home() / ".local" / "share"

    log_directory = base_directory / "NetGuardianPro" / "logs"
    log_directory.mkdir(parents=True, exist_ok=True)
    return log_directory


LOG_DIRECTORY = _get_log_directory()
LOG_FILE = LOG_DIRECTORY / "app.log"

logger = logging.getLogger("NetGuardianPro")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)


def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message, include_traceback=False):
    logger.error(message, exc_info=include_traceback)


def get_log_file_path():
    return str(LOG_FILE)