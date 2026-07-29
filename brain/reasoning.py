"""
==========================================
Reasoning Engine
Nova-Trader-BM
==========================================
"""


class Reasoning:

    def explain(

        self,

        trend,

        indicators,

        confidence

    ):

        reasons = []

        reasons.append(f"Trend: {trend}")

        reasons.append(

            f"RSI: {round(indicators['rsi'],2)}"

        )

        reasons.append(

            f"MACD: {round(indicators['macd'],5)}"

        )

        reasons.append(

            f"Confidence: {confidence}"

        )

        return reasons
