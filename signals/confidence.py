"""
==========================================
Signal Confidence
Nova-Trader-BM
==========================================
"""


class ConfidenceCalculator:

    def calculate(self, score, maximum):

        if maximum <= 0:

            return 0

        return round((score / maximum) * 100)
