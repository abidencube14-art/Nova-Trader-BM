"""
==========================================
Profit Factor
Nova-Trader-BM
==========================================
"""


class ProfitFactor:

    def calculate(

        self,

        gross_profit,

        gross_loss

    ):

        if gross_loss == 0:

            return 0

        return round(

            gross_profit /

            abs(gross_loss),

            2

        )
