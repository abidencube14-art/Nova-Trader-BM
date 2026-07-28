"""
==========================================
Logger
Nova-Trader-BM
==========================================
"""

import logging
import os

LOG_FOLDER = "logs"

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, "bot.log"),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def info(message):
    logging.info(message)
    print("[INFO]", message)


def warning(message):
    logging.warning(message)
    print("[WARNING]", message)


def error(message):
    logging.error(message)
    print("[ERROR]", message)
