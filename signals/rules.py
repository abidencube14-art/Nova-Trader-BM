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
        # TREND ALIGNMENT
        # ----------------------------------

        bullish_trend = (
            ema20 > ema50
            and ema50 > ema200
        )

        bearish_trend = (
            ema20 < ema50
            and ema50 < ema200
        )

        # ----------------------------------
        # BULLISH SETUP
        # ----------------------------------

        if bullish_trend:

            buy_score += 2

            buy_reasons.append(
                "Bullish EMA alignment"
            )

            # MACD confirmation

            if macd > signal:

                buy_score += 1

                buy_reasons.append(
                    "MACD bullish"
                )

            # RSI confirmation

            if 40 <= rsi <= 65:

                buy_score += 1

                buy_reasons.append(
                    "RSI supports BUY"
                )

            elif rsi < 40:

                buy_score += 1

                buy_reasons.append(
                    "RSI recovering from oversold"
                )

            elif rsi > 70:

                buy_score -= 1

                buy_reasons.append(
                    "RSI overbought"
                )

        # ----------------------------------
        # BEARISH SETUP
        # ----------------------------------

        elif bearish_trend:

            sell_score += 2

            sell_reasons.append(
                "Bearish EMA alignment"
            )

            # MACD confirmation

            if macd < signal:

                sell_score += 1

                sell_reasons.append(
                    "MACD bearish"
                )

            # RSI confirmation

            if 35 <= rsi <= 60:

                sell_score += 1

                sell_reasons.append(
                    "RSI supports SELL"
                )

            elif rsi > 60:

                sell_score += 1

                sell_reasons.append(
                    "RSI rejecting overbought zone"
                )

            elif rsi < 30:

                sell_score -= 1

                sell_reasons.append(
                    "RSI oversold"
                )

        # ----------------------------------
        # NO CLEAR TREND
        # ----------------------------------

        else:

            return (
                0,
                "WAIT",
                [
                    "EMA trend alignment is unclear"
                ]
            )

        # ----------------------------------
        # FINAL RESULT
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
                "Signal confirmation is insufficient"
            ]
            )
