"""
==========================================
Trade Entry Logic
Nova-Trader-BM
==========================================
"""

from strategy.trend import detect_trend
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd


def entry_signal(data):

    trend = detect_trend(data)

    rsi = calculate_rsi(data)

    macd, signal, histogram = calculate_macd(data)

    latest_rsi = rsi.iloc[-1]

    latest_macd = macd.iloc[-1]

    latest_signal = signal.iloc[-1]

    if (
        trend == "BUY"
        and latest_rsi > 55
        and latest_macd > latest_signal
    ):
        return "BUY"

    if (
        trend == "SELL"
        and latest_rsi < 45
        and latest_macd < latest_signal
    ):
        return "SELL"

    return "WAIT"
