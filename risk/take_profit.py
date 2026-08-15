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

        action,

        multiplier=3

    ):

        if action == "SELL":

            return entry - (

                atr * multiplier

            )

        return entry + (

            atr * multiplier

        )
