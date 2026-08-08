"""
==========================================
Simulator Execution
Nova-Trader-BM
==========================================
"""

from simulator.position import Position


class SimulatorExecution:

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

    def close_trade(

        self,

        position,

        current_price,

        reason

    ):

        if position.status != "OPEN":

            return position

        position.exit_price = current_price

        if position.action == "BUY":

            position.profit_loss = (

                current_price - position.entry

            ) * position.lot

        elif position.action == "SELL":

            position.profit_loss = (

                position.entry - current_price

            ) * position.lot

        position.status = "CLOSED"

        position.close_reason = reason

        return position
