"""
==========================================
Trend Analysis
Nova-Trader-BM
==========================================
"""


class TrendAnalysis:

    def detect(self, indicators):

        ema20 = indicators["ema20"]
        ema50 = indicators["ema50"]
        ema200 = indicators["ema200"]

        if ema20 > ema50 > ema200:

            return "BULLISH"

        elif ema20 < ema50 < ema200:

            return "BEARISH"

        return "SIDEWAYS"
