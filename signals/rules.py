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

        ema20 = indicators["ema20"]
        ema50 = indicators["ema50"]
        ema200 = indicators["ema200"]

        macd = indicators["macd"]
        signal = indicators["signal"]

        # ----------------------------------
        # EMA20 / EMA50
        # ----------------------------------

        if ema20 > ema50:

            buy_score += 1

            buy_reasons.append(
                "EMA20 above EMA50"
            )

        elif ema20 < ema50:

            sell_score += 1

            sell_reasons.append(
                "EMA20 below EMA50"
            )

        # ----------------------------------
        # EMA50 / EMA200
        # ----------------------------------

        if ema50 > ema200:

            buy_score += 1

            buy_reasons.append(
                "EMA50 above EMA200"
            )

        elif ema50 < ema200:

            sell_score += 1

            sell_reasons.append(
                "EMA50 below EMA200"
            )

        # ----------------------------------
        # MACD MOMENTUM
        # ----------------------------------

        if macd > signal:

            buy_score += 1

            buy_reasons.append(
                "MACD bullish"
            )

        elif macd < signal:

            sell_score += 1

            sell_reasons.append(
                "MACD bearish"
            )

        # ----------------------------------
        # RSI
        # ----------------------------------

        # Healthy bullish RSI
        if 50 <= rsi <= 65:

            buy_score += 1

            buy_reasons.append(
                "RSI supports BUY"
            )

        # Healthy bearish RSI
        elif 35 <= rsi < 50:

            sell_score += 1

            sell_reasons.append(
                "RSI supports SELL"
            )

        # ----------------------------------
        # EXTREME RSI CONDITIONS
        # ----------------------------------

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
        # FINAL DECISION
        # ----------------------------------

        # Strong BUY requires:
        # - at least 3 BUY points
        # - BUY must clearly beat SELL

        if buy_score >= 3 and buy_score > sell_score:

            return (
                buy_score,
                "BUY",
                buy_reasons
            )

        # Strong SELL requires:
        # - at least 3 SELL points
        # - SELL must clearly beat BUY

        if sell_score >= 3 and sell_score > buy_score:

            return (
                sell_score,
                "SELL",
                sell_reasons
            )

        # ----------------------------------
        # CONFLICT / WEAK SIGNAL
        # ----------------------------------

        return (
            max(buy_score, sell_score),
            "WAIT",
            [
                "Signal confirmation insufficient"
            ]
        )
