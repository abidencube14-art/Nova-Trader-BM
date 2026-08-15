"""
==========================================
Signal Confidence
Nova-Trader-BM
==========================================
"""


class ConfidenceCalculator:

    def calculate(
        self,
        score,
        maximum
    ):

        if maximum <= 0:
            return 0

        if score <= 0:
            return 0

        confidence = (
            score / maximum
        ) * 100

        return round(
            min(confidence, 100)
        )
