"""
==========================================
Take Profit
Nova-Trader-BM
==========================================
"""


class TakeProfit:

    def calculate(

        self,

        entry,

        atr,

        multiplier=3

    ):

        return entry + (

            atr * multiplier

        )
