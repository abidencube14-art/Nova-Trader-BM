"""
==========================================
Trend Detection
Nova-Trader-BM
==========================================
"""

from indicators.ema import calculate_ema


def detect_trend(data, fast_period=50, slow_period=200):

    ema_fast = calculate_ema(data, fast_period)

    ema_slow = calculate_ema(data, slow_period)

    if ema_fast.iloc[-1] > ema_slow.iloc[-1]:
        return "BUY"

    elif ema_fast.iloc[-1] < ema_slow.iloc[-1]:
        return "SELL"

    return "SIDEWAYS"
