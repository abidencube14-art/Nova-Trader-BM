"""
==========================================
Backtest Report
Nova-Trader-BM
==========================================
"""

class Report:

    def generate(

        self,

        stats

    ):

        print(

            "=========="

        )

        print(

            "BACKTEST"

        )

        print(

            "=========="

        )

        for key, value in stats.items():

            print(

                f"{key}: {value}"

            )
