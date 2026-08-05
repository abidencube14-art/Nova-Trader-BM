"""
==========================================
Simulator Engine
Nova-Trader-BM
==========================================
"""

from simulator.account import SimulatorAccount
from simulator.execution import SimulatorExecution
from simulator.history import TradeHistory


class SimulatorEngine:

    def __init__(self):

        self.account = SimulatorAccount()

        self.execution = SimulatorExecution()

        self.history = TradeHistory()

    def execute(

        self,

        symbol,

        decision,

        risk,

        entry

    ):

        if decision.action == "WAIT":

            return None

        if risk is None:

            return None

        trade = self.execution.open_trade(

            symbol,

            decision.action,

            risk["lot"],

            entry,

            risk["sl"],

            risk["tp"]

        )

        self.history.add(trade)

        return trade
