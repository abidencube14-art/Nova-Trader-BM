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

        # Commission charged per completed trade.
        self.commission = 0.01

        # Standard FX contract size.
        self.contract_size = 100000

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

        # ----------------------------------
        # BUY
        # ----------------------------------

        if trade.action == "BUY":

            if low <= trade.sl:

                exit_price = trade.sl

                close_reason = "STOP_LOSS"

            elif high >= trade.tp:

                exit_price = trade.tp

                close_reason = "TAKE_PROFIT"

        # ----------------------------------
        # SELL
        # ----------------------------------

        elif trade.action == "SELL":

            if high >= trade.sl:

                exit_price = trade.sl

                close_reason = "STOP_LOSS"

            elif low <= trade.tp:

                exit_price = trade.tp

                close_reason = "TAKE_PROFIT"

        if exit_price is None:

            return trade

        # ----------------------------------
        # Close trade
        # ----------------------------------

        trade = self.execution.close_trade(

            trade,

            exit_price,

            close_reason

        )

        # ----------------------------------
        # Calculate monetary P/L correctly
        # ----------------------------------

        price_difference = (

            exit_price - trade.entry

        )

        if trade.action == "SELL":

            price_difference = (

                trade.entry - exit_price

            )

        units = (

            trade.lot

            * self.contract_size

        )

        # ----------------------------------
        # USD-quoted pairs
        #
        # EURUSD
        # GBPUSD
        # AUDUSD
        # ----------------------------------

        if trade.symbol.endswith("USD"):

            profit_loss = (

                price_difference

                * units

            )

        # ----------------------------------
        # USD-base pairs
        #
        # USDJPY
        #
        # Convert JPY P/L back to USD.
        # ----------------------------------

        elif trade.symbol.startswith("USD"):

            if exit_price <= 0:

                profit_loss = 0.0

            else:

                profit_loss = (

                    price_difference

                    * units

                    / exit_price

                )

        # ----------------------------------
        # Fallback for other currency pairs
        # ----------------------------------

        else:

            profit_loss = (

                price_difference

                * units

            )

        trade.profit_loss = round(

            profit_loss,

            2

        )

        # ----------------------------------
        # Commission
        # ----------------------------------

        trade.profit_loss = round(

            trade.profit_loss

            - self.commission,

            2

        )

        # ----------------------------------
        # Update account
        # ----------------------------------

        self.account.apply_profit_loss(

            trade.profit_loss

        )

        return trade
