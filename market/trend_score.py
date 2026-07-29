"""
==========================================
Trend Score
Nova-Trader-BM
==========================================
"""


class TrendScore:

    def calculate(

        self,

        ema50,

        ema200

    ):

        difference = abs(ema50 - ema200)

        if difference > 0.0100:

            return 25

        elif difference > 0.0050:

            return 20

        elif difference > 0.0025:

            return 15

        return 5
