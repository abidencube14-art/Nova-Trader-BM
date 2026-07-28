"""
==========================================
ATR Indicator
Nova-Trader-BM
==========================================
"""

import pandas as pd


def calculate_atr(data, period=14):

    high_low = data["high"] - data["low"]

    high_close = (data["high"] - data["close"].shift()).abs()

    low_close = (data["low"] - data["close"].shift()).abs()

    true_range = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)

    atr = true_range.rolling(period).mean()

    return atr
