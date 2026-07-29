"""
==========================================
Learning Statistics
Nova-Trader-BM
==========================================
"""

class LearningStatistics:

    def report(

        self,

        experience

    ):

        total = experience["total"]

        if total == 0:

            return {}

        win_rate = (

            experience["wins"]

            /

            total

        ) * 100

        return {

            "Trades": total,

            "Win Rate": round(win_rate,2)

        }
