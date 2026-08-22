"""
==========================================
Simulator Execution
Nova-Trader-BM
==========================================
"""

from simulator.position import Position


class SimulatorExecution:

    # ======================================
    # OPEN TRADE
    # ======================================

    def open_trade(

        self,

        symbol,

        action,

        lot,

        entry,

        sl,

        tp

    ):

        return Position(

            symbol,

            action,

            lot,

            entry,

            sl,

            tp

        )

    # ======================================
    # CLOSE TRADE
    # ======================================

    def close_trade(

        self,

        position,

        current_price,

        reason

    ):

        # ----------------------------------
        # Already closed
        # ----------------------------------

        if position.status != "OPEN":

            return position

        # ----------------------------------
        # Store exit information
        # ----------------------------------

        position.exit_price = current_price

        position.close_reason = reason

        # ----------------------------------
        # P/L is NOT calculated here.
        #
        # SimulatorEngine is responsible
        # for calculating monetary P/L.
        # ----------------------------------

        position.status = "CLOSED"

        return position
