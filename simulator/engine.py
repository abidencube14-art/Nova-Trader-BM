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

    def check_exit(

        self,

        trade,

        high,

        low

    ):

        if trade is None:

            return None

        if trade.status == "CLOSED":

            return trade

        exit_price = None

        close_reason = None

        if trade.action == "BUY":

            if low <= trade.sl:

                exit_price = trade.sl

                close_reason = "STOP_LOSS"

            elif high >= trade.tp:

                exit_price = trade.tp

                close_reason = "TAKE_PROFIT"

        elif trade.action == "SELL":

            if high >= trade.sl:

                exit_price = trade.sl

                close_reason = "STOP_LOSS"

            elif low <= trade.tp:

                exit_price = trade.tp

                close_reason = "TAKE_PROFIT"

        if exit_price is None:

            return trade

        trade = self.execution.close_trade(

            trade,

            exit_price,

            close_reason

        )

        trade.profit_loss = round(

            trade.profit_loss * 100000,

            2

        )

        self.account.apply_profit_loss(

            trade.profit_loss

        )

        return trade

        profit_loss = (

            price_difference

            * trade.lot

            * 100000

        )

        trade.exit_price = exit_price

        trade.profit_loss = round(

            profit_loss,

            2

        )

        trade.close_reason = close_reason

        trade.status = "CLOSED"

        self.account.deposit(

            trade.profit_loss

        )

        return trade
