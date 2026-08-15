"""
==========================================
Trading Rules
Nova-Trader-BM
==========================================
"""


class TradingRules:

    def evaluate(self, indicators):

        buy_score = 0
        sell_score = 0

        buy_reasons = []
        sell_reasons = []

        rsi = indicators["rsi"]

        # ----------------------------------
        # SHORT-TERM EMA TREND
        # ----------------------------------

        if indicators["ema20"] > indicators["ema50"]:

            buy_score += 1

            buy_reasons.append(
                "EMA20 above EMA50"
            )

        elif indicators["ema20"] < indicators["ema50"]:

            sell_score += 1

            sell_reasons.append(
                "EMA20 below EMA50"
            )

        # ----------------------------------
        # LONG-TERM EMA TREND
        # ----------------------------------

        if indicators["ema50"] > indicators["ema200"]:

            buy_score += 1

            buy_reasons.append(
                "EMA50 above EMA200"
            )

        elif indicators["ema50"] < indicators["ema200"]:

            sell_score += 1

            sell_reasons.append(
                "EMA50 below EMA200"
            )

        # ----------------------------------
        # MACD MOMENTUM
        # ----------------------------------

        if indicators["macd"] > indicators["signal"]:

            buy_score += 1

            buy_reasons.append(
                "MACD bullish"
            )

        elif indicators["macd"] < indicators["signal"]:

            sell_score += 1

            sell_reasons.append(
                "MACD bearish"
            )

        # ----------------------------------
        # RSI
        # ----------------------------------

        # Bullish momentum zone
        if 40 <= rsi < 65:

            buy_score += 1

            buy_reasons.append(
                "RSI supports bullish momentum"
            )

        # Bearish momentum zone
        elif 35 < rsi <= 60:

            sell_score += 1

            sell_reasons.append(
                "RSI supports bearish momentum"
            )

        # Oversold
        elif rsi <= 35:

            buy_score += 1

            buy_reasons.append(
                "RSI oversold"
            )

        # Overbought
        elif rsi >= 65:

            sell_score += 1

            sell_reasons.append(
                "RSI overbought"
            )

        # ----------------------------------
        # FINAL DIRECTION
        # ----------------------------------

        if buy_score > sell_score:

            return (
                buy_score,
                "BUY",
                buy_reasons
            )

        if sell_score > buy_score:

            return (
                sell_score,
                "SELL",
                sell_reasons
            )

        return (
            0,
            "WAIT",
            [
                "BUY and SELL scores are equal"
            ]
            )
