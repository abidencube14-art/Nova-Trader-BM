"""
==========================================
Position Size Calculator
Nova-Trader-BM
==========================================
"""


class PositionSizer:

    def calculate(

        self,

        balance,

        risk_percent,

        stop_loss_pips,

        pip_value

    ):

        if balance <= 0:

            return 0.0

        if stop_loss_pips <= 0:

            return 0.0

        if pip_value <= 0:

            return 0.0

        risk_amount = balance * (

            risk_percent / 100

        )

        lot = risk_amount / (

            stop_loss_pips * pip_value

        )

        return round(lot, 5)
