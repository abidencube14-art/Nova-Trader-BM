"""
==========================================
EMA Indicator
Nova-Trader-BM
==========================================
"""

import pandas as pd


def calculate_ema(data, period):
    """
    Calculate Exponential Moving Average.
    """

    return data["close"].ewm(span=period, adjust=False).mean()
