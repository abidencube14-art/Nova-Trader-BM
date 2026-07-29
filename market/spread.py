"""
==========================================
Spread Filter
Nova-Trader-BM
==========================================
"""


class SpreadFilter:

    def acceptable(

        self,

        spread,

        maximum=20

    ):

        return spread <= maximum
