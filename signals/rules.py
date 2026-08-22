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

        # ----------------------------------
        # Read indicators
        # ----------------------------------

        rsi = indicators["rsi"]

        ema20 = indicators["ema20"]
        ema50 = indicators["ema50"]
        ema200 = indicators["ema200"]

        macd = indicators["macd"]
        signal = indicators["signal"]

        # ----------------------------------
        # EMA TREND
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
        # MACD MOMENTUM
        # ----------------------------------

        bullish_momentum = (

            macd > signal

        )

        bearish_momentum = (

            macd < signal

        )

        # ----------------------------------
        # RSI FILTER
        #
        # RSI > 70 = overbought
        # RSI < 30 = oversold
        #
        # Extreme RSI does NOT automatically
        # create a reversal trade.
        # It blocks the normal trend entry.
        # ----------------------------------

        bullish_rsi = (

            50 <= rsi <= 70

        )

        bearish_rsi = (

            30 <= rsi < 50

        )

        # ----------------------------------
        # SCORE BUY CONDITIONS
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
        # MACD
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

        if bullish_rsi:

            buy_score += 1

            buy_reasons.append(
                "RSI supports BUY"
            )

        elif bearish_rsi:

            sell_score += 1

            sell_reasons.append(
                "RSI supports SELL"
            )

        # ----------------------------------
        # EXTREME RSI PROTECTION
        # ----------------------------------

        if rsi > 70:

            return (

                buy_score,

                "WAIT",

                [
                    "RSI overbought - BUY blocked"
                ]

            )

        if rsi < 30:

            return (

                sell_score,

                "WAIT",

                [
                    "RSI oversold - SELL blocked"
                ]

            )

        # ----------------------------------
        # STRONG BUY
        #
        # All three major confirmations
        # must agree:
        #
        # EMA trend
        # MACD momentum
        # RSI
        # ----------------------------------

        if (

            bullish_trend
            and bullish_momentum
            and bullish_rsi
            and buy_score == 4

        ):

            return (

                buy_score,

                "BUY",

                buy_reasons

            )

        # ----------------------------------
        # STRONG SELL
        # ----------------------------------

        if (

            bearish_trend
            and bearish_momentum
            and bearish_rsi
            and sell_score == 4

        ):

            return (

                sell_score,

                "SELL",

                sell_reasons

            )

        # ----------------------------------
        # WAIT
        # ----------------------------------

        return (

            max(
                buy_score,
                sell_score
            ),

            "WAIT",

            [
                "Signal confirmation insufficient"
            ]

        )
