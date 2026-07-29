"""
==========================================
Trade Entries
Nova-Trader-BM
==========================================
"""

from strategy.trend import detect_trend


def entry_signal(indicators):

    trend = detect_trend(indicators)

    if (

        trend == "BUY"

        and indicators["rsi"] > 55

        and indicators["macd"] > indicators["signal"]

    ):

        return "BUY"

    if (

        trend == "SELL"

        and indicators["rsi"] < 45

        and indicators["macd"] < indicators["signal"]

    ):

        return "SELL"

    return "WAIT"
