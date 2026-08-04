"""
==========================================
Backtest Statistics
Nova-Trader-BM
==========================================
"""

class Statistics:

    def calculate(self, trades):

        total = len(trades)

        wins = len(

            [

                t for t in trades

                if t.profit > 0

            ]

        )

        losses = total - wins

        win_rate = 0

        if total > 0:

            win_rate = (

                wins / total

            ) * 100

        return {

            "total": total,

            "wins": wins,

            "losses": losses,

            "win_rate": round(

                win_rate,

                2

            )

        }
