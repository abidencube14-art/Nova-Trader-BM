"""
==========================================
Stop Loss
Nova-Trader-BM
==========================================
"""


class StopLoss:

    def calculate(

        self,

        entry,

        atr,

        multiplier=2

    ):

        return entry - (

            atr * multiplier

        )
