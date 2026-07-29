"""
==========================================
Trend Strength
Nova-Trader-BM
==========================================
"""


class TrendStrength:

    def calculate(self, indicators):

        difference = abs(

            indicators["ema50"]

            -

            indicators["ema200"]

        )

        return round(difference, 5)
