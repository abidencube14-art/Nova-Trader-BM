"""
==========================================
Confidence Level
Nova-Trader-BM
==========================================
"""


class Confidence:

    def level(self, score):

        if score >= 90:

            return "VERY HIGH"

        elif score >= 75:

            return "HIGH"

        elif score >= 60:

            return "MEDIUM"

        elif score >= 40:

            return "LOW"

        return "AVOID"
