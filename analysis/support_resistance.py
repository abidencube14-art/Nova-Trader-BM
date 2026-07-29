"""
==========================================
Support & Resistance
Nova-Trader-BM
==========================================
"""


class SupportResistance:

    def support(self, data, period=20):

        return data["low"].tail(period).min()

    def resistance(self, data, period=20):

        return data["high"].tail(period).max()
