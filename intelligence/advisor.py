"""
==========================================
Trading Advisor
Nova-Trader-BM
==========================================
"""


class TradingAdvisor:

    def advice(

        self,

        score

    ):

        if score >= 90:

            return "EXECUTE"

        elif score >= 75:

            return "WATCH"

        elif score >= 60:

            return "WAIT"

        return "IGNORE"
