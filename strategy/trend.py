"""
==========================================
Trend Detection
Nova-Trader-BM
==========================================
"""


def detect_trend(indicators):

    if indicators["ema50"] > indicators["ema200"]:

        return "BUY"

    if indicators["ema50"] < indicators["ema200"]:

        return "SELL"

    return "SIDEWAYS"
