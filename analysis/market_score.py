"""
==========================================
Market Score
Nova-Trader-BM
==========================================
"""


class MarketScore:

    def calculate(

        self,

        indicators,

        trend,

        candle_confirmation

    ):

        score = 0

        if trend == "BULLISH":
            
            score += 40

        elif trend == "BEARISH":
            
            score += 40

        if indicators["rsi"] > 55:

            score += 20

        elif indicators["rsi"] < 45:

            score += 20

        if candle_confirmation:

            score += 40

        return score
