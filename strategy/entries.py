"""
==========================================
Trade Entries
Nova-Trader-BM
==========================================
"""

from strategy.trend import detect_trend


def entry_signal(

    indicators,

    market

)::

    trend = detect_trend(indicators)

    if (

    trend == "BUY"

    and market["structure"] == "UPTREND"

    and indicators["rsi"] > 55

    and indicators["macd"] > indicators["signal"]

):

        return "BUY"

    if (

    trend == "SELL"

    and market["structure"] == "DOWNTREND"

    and indicators["rsi"] < 45

    and indicators["macd"] < indicators["signal"]

):

        return "SELL"

    return "WAIT"
