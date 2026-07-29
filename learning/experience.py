"""
==========================================
Experience Engine
Nova-Trader-BM
==========================================
"""

class Experience:

    def analyse(self, trades):

        wins = 0
        losses = 0

        for trade in trades:

            if trade["profit"] > 0:

                wins += 1

            else:

                losses += 1

        return {

            "wins": wins,

            "losses": losses,

            "total": len(trades)

        }
