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
