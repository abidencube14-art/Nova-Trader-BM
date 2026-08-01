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

        risk_amount = balance * (

            risk_percent / 100

        )

        lot = risk_amount / (

            stop_loss_pips * pip_value

        )

        return round(lot, 2)
