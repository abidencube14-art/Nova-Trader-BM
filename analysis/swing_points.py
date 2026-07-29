"""
==========================================
Swing High / Low Detection
Nova-Trader-BM
==========================================
"""


class SwingPoints:

    def swing_high(self, data):

        return data["high"].tail(20).max()

    def swing_low(self, data):

        return data["low"].tail(20).min()
