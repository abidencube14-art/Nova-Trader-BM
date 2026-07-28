"""
==========================================
Time Utilities
Nova-Trader-BM
==========================================
"""

from datetime import datetime


def now():

    return datetime.now()


def timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
