"""
==========================================
Trading Rules
Nova-Trader-BM
==========================================
"""


class TradingRules:

    def evaluate(self, indicators):

        score = 0

        reasons = []

        # Trend

        if indicators["ema20"] > indicators["ema50"]:

            score += 1

            reasons.append("EMA20 above EMA50")

        if indicators["ema50"] > indicators["ema200"]:

            score += 1

            reasons.append("EMA50 above EMA200")

        # Momentum

        if indicators["macd"] > indicators["signal"]:

            score += 1

            reasons.append("MACD bullish")

        # RSI

        if 50 <= indicators["rsi"] <= 70:

            score += 1

            reasons.append("Healthy RSI")

        return score, reasons
