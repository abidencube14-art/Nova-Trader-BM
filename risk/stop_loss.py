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

        action,

        multiplier=2

    ):

        if action == "SELL":

            return entry + (

                atr * multiplier

            )

        return entry - (

            atr * multiplier

        )
