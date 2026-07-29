"""
==========================================
Mistake Detector
Nova-Trader-BM
==========================================
"""

class MistakeDetector:

    def analyse(self, trades):

        mistakes = []

        for trade in trades:

            if trade["profit"] < 0:

                mistakes.append({

                    "symbol": trade["symbol"],

                    "reason": "Loss"

                })

        return mistakes
