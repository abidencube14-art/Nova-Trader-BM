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

        # ----------------------------------
        # Validate inputs
        # ----------------------------------

        if balance <= 0:

            return 0.0

        if risk_percent <= 0:

            return 0.0

        if stop_loss_pips <= 0:

            return 0.0

        if pip_value <= 0:

            return 0.0

        # ----------------------------------
        # Maximum money we are willing
        # to lose if SL is hit
        # ----------------------------------

        risk_amount = (

            balance
            * risk_percent
            / 100

        )

        # ----------------------------------
        # Position size
        # ----------------------------------

        lot = (

            risk_amount
            / (
                stop_loss_pips
                * pip_value
            )

        )

        # ----------------------------------
        # Safety
        # ----------------------------------

        if lot <= 0:

            return 0.0

        return round(

            lot,

            5

        )
