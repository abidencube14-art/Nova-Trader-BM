"""
==========================================
Volatility Analysis
Nova-Trader-BM
==========================================
"""


class VolatilityAnalysis:

    def classify(self, atr):

        if atr <= 0:
            return "LOW"

        elif atr < 0.001:
            return "NORMAL"

        return "HIGH"
