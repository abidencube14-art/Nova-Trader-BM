"""
==========================================
Learning Recommendation
Nova-Trader-BM
==========================================
"""


class Recommendation:

    def next_action(

        self,

        confidence,

        win_rate

    ):

        if confidence == "VERY HIGH" and win_rate >= 70:

            return "CONTINUE"

        if win_rate < 50:

            return "REVIEW STRATEGY"

        return "MONITOR"
