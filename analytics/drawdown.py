"""
==========================================
Drawdown Calculator
Nova-Trader-BM
==========================================
"""


class Drawdown:

    def calculate(

        self,

        peak,

        balance

    ):

        if peak == 0:

            return 0

        value = (

            (peak - balance)

            /

            peak

        ) * 100

        return round(value, 2)
