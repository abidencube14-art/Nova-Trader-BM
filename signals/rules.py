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
        # EMA TREND
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
        # LONG-TERM TREND
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

        if 30 <= rsi <= 70:

            if rsi <= 50:

                buy_score += 1

                buy_reasons.append(
                    "RSI supports BUY"
                )

            if rsi >= 50:

                sell_score += 1

                sell_reasons.append(
                    "RSI supports SELL"
                )

        elif rsi > 70:

            sell_score += 1

            sell_reasons.append(
                "RSI overbought"
            )

        elif rsi < 30:

            buy_score += 1

            buy_reasons.append(
                "RSI oversold"
            )

        # ----------------------------------
        # Final result
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
        # Momentum

        if indicators["macd"] > indicators["signal"]:

            score += 1

            reasons.append("MACD bullish")

        # RSI

        if 50 <= indicators["rsi"] <= 70:

            score += 1

            reasons.append("Healthy RSI")

        return score, reasons
