"""
==========================================
Safety Controller
Nova-Trader-BM
==========================================
"""


class SafetyController:

    def allow_trade(

        self,

        confidence,

        risk_ok,

        spread_ok

    ):

        if confidence not in (

            "HIGH",

            "VERY HIGH"

        ):

            return False

        if not risk_ok:

            return False

        if not spread_ok:

            return False

        return True
