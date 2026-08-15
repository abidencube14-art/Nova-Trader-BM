"""
==========================================
RSI Indicator
Nova-Trader-BM
==========================================
"""

import pandas as pd


def calculate_rsi(data, period=14):

    delta = data["close"].diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(
        alpha=1 / period,
        adjust=False,
        min_periods=period
    ).mean()

    avg_loss = loss.ewm(
        alpha=1 / period,
        adjust=False,
        min_periods=period
    ).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (
        100 / (1 + rs)
    )

    rsi = rsi.clip(
        lower=0,
        upper=100
    )

    return rsi
