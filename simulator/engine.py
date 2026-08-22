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

        # ----------------------------------
        # Simulation settings
        # ----------------------------------

        self.commission = 0.01

        self.contract_size = 100000

        # Exit diagnostics
        self.exit_count = 0

    # ======================================
    # EXECUTE TRADE
    # ======================================

    def execute(

        self,
        symbol,
        decision,
        risk,
        entry

    ):

        if decision is None:

            return None

        if decision.action == "WAIT":

            return None

        if risk is None:

            return None

        lot = risk.get("lot", 0)

        sl = risk.get("sl")

        tp = risk.get("tp")

        if lot <= 0:

            return None

        if sl is None or tp is None:

            return None

        # ----------------------------------
        # Open position
        # ----------------------------------

        trade = self.execution.open_trade(

            symbol,
            decision.action,
            lot,
            entry,
            sl,
            tp

        )

        self.history.add(trade)

        # ----------------------------------
        # Trade diagnostic
        # ----------------------------------

        if len(self.history.trades) <= 5:

            print()

            print("-----------------------------------")
            print("NOVA TRADE DIAGNOSTIC")
            print("-----------------------------------")

            print(
                f"Symbol : {symbol}"
            )

            print(
                f"Action : {trade.action}"
            )

            print(
                f"Lot    : {trade.lot}"
            )

            print(
                f"Entry  : {trade.entry}"
            )

            print(
                f"SL     : {trade.sl}"
            )

            print(
                f"TP     : {trade.tp}"
            )

            print("-----------------------------------")

        return trade

    # ======================================
    # CHECK EXIT
    # ======================================

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

        stop_hit = False

        target_hit = False

        # ==================================
        # BUY POSITION
        # ==================================

        if trade.action == "BUY":

            stop_hit = (

                low <= trade.sl

            )

            target_hit = (

                high >= trade.tp

            )

            if stop_hit:

                exit_price = trade.sl

                close_reason = "STOP_LOSS"

            elif target_hit:

                exit_price = trade.tp

                close_reason = "TAKE_PROFIT"

        # ==================================
        # SELL POSITION
        # ==================================

        elif trade.action == "SELL":

            stop_hit = (

                high >= trade.sl

            )

            target_hit = (

                low <= trade.tp

            )

            if stop_hit:

                exit_price = trade.sl

                close_reason = "STOP_LOSS"

            elif target_hit:

                exit_price = trade.tp

                close_reason = "TAKE_PROFIT"

        # ==================================
        # No exit
        # ==================================

        if exit_price is None:

            return trade

        # ==================================
        # Close position
        # ==================================

        trade = self.execution.close_trade(

            trade,
            exit_price,
            close_reason

        )

        # ==================================
        # Calculate REAL FX P/L
        # ==================================

        price_difference = (

            exit_price - trade.entry

        )

        if trade.action == "SELL":

            price_difference = (

                trade.entry - exit_price

            )

        # ==================================
        # Convert lots to units
        # ==================================

        units = (

            trade.lot
            * self.contract_size

        )

        # ==================================
        # USD-QUOTED PAIRS
        # EURUSD
        # GBPUSD
        # AUDUSD
        # ==================================

        if trade.symbol.endswith("USD"):

            profit_loss = (

                price_difference
                * units

            )

        # ==================================
        # USD-BASE PAIRS
        # USDJPY
        # ==================================

        elif trade.symbol.startswith("USD"):

            if exit_price <= 0:

                profit_loss = 0.0

            else:

                profit_loss = (

                    price_difference
                    * units
                    / exit_price

                )

        # ==================================
        # FALLBACK
        # ==================================

        else:

            profit_loss = (

                price_difference
                * units

            )

        # ==================================
        # Commission
        # ==================================

        profit_loss -= self.commission

        # ==================================
        # Store P/L
        # ==================================

        trade.profit_loss = round(

            profit_loss,
            5

        )

        # ==================================
        # Update account
        # ==================================

        self.account.apply_profit_loss(

            trade.profit_loss

        )

        # ==================================
        # EXIT DIAGNOSTIC
        # ==================================

        self.exit_count += 1

        if self.exit_count <= 15:

            print()

            print("-----------------------------------")
            print("NOVA EXIT DIAGNOSTIC")
            print("-----------------------------------")

            print(
                f"Symbol      : {trade.symbol}"
            )

            print(
                f"Action      : {trade.action}"
            )

            print(
                f"Entry       : {trade.entry}"
            )

            print(
                f"Candle High : {high}"
            )

            print(
                f"Candle Low  : {low}"
            )

            print(
                f"SL          : {trade.sl}"
            )

            print(
                f"TP          : {trade.tp}"
            )

            print(
                f"Stop Hit    : {stop_hit}"
            )

            print(
                f"Target Hit  : {target_hit}"
            )

            print(
                f"Exit Price  : {exit_price}"
            )

            print(
                f"Reason      : {close_reason}"
            )

            print(
                f"P/L         : ${trade.profit_loss:.5f}"
            )

            print("-----------------------------------")

        return trade
