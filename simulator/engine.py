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

        # Small fixed commission per completed trade.
        self.commission = 0.01

        # Standard FX contract size.
        self.contract_size = 100000

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

        # ----------------------------------
        # Ignore WAIT
        # ----------------------------------

        if decision is None:

            return None

        if decision.action == "WAIT":

            return None

        # ----------------------------------
        # Risk must exist
        # ----------------------------------

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
        # TRADE DIAGNOSTIC
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

            # ----------------------------------
            # Conservative assumption:
            #
            # If both SL and TP occur inside
            # the same candle, assume SL was hit
            # first.
            # ----------------------------------

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

            # ----------------------------------
            # Conservative assumption:
            # SL first if both are touched.
            # ----------------------------------

            if stop_hit:

                exit_price = trade.sl

                close_reason = "STOP_LOSS"

            elif target_hit:

                exit_price = trade.tp

                close_reason = "TAKE_PROFIT"

        # ==================================
        # No exit yet
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

        # ----------------------------------
        # Convert lots to units
        # ----------------------------------

        units = (

            trade.lot
            * self.contract_size

        )

        # ==================================
        # USD-QUOTED PAIRS
        #
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
        #
        # USDJPY
        #
        # Price difference is in JPY.
        # Convert JPY profit/loss back to USD.
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
        # Apply commission
        # ==================================

        profit_loss -= self.commission

        # ----------------------------------
        # Round monetary result
        # ----------------------------------

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

        return trade
