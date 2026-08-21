"""
==========================================
Risk Engine
Nova-Trader-BM
==========================================
"""

from risk.position_size import PositionSizer
from risk.stop_loss import StopLoss
from risk.take_profit import TakeProfit
from risk.filters import RiskFilters


class RiskEngine:

    def __init__(self):

        self.sizer = PositionSizer()

        self.sl = StopLoss()

        self.tp = TakeProfit()

        self.filters = RiskFilters()

    def evaluate(

        self,

        decision,

        symbol,

        balance,

        entry,

        atr

    ):

        # ----------------------------------
        # Signal permission
        # ----------------------------------

        if not self.filters.allow(decision):

            return None

        # ----------------------------------
        # Validate market data
        # ----------------------------------

        if balance <= 0:

            return None

        if entry <= 0:

            return None

        if atr <= 0:

            return None

        # ----------------------------------
        # Direction-aware SL
        # ----------------------------------

        sl = self.sl.calculate(

            entry,

            atr,

            decision.action

        )

        # ----------------------------------
        # Direction-aware TP
        # ----------------------------------

        tp = self.tp.calculate(

            entry,

            atr,

            decision.action

        )

        # ----------------------------------
        # Actual stop distance
        # ----------------------------------

        stop_distance = abs(

            entry - sl

        )

        if stop_distance <= 0:

            return None

        # ----------------------------------
        # Pair pip size
        # ----------------------------------

        if symbol.endswith("JPY"):

            pip_size = 0.01

        else:

            pip_size = 0.0001

        # ----------------------------------
        # Stop distance in pips
        # ----------------------------------

        stop_loss_pips = (

            stop_distance
            / pip_size

        )

        if stop_loss_pips <= 0:

            return None

        # ----------------------------------
        # Pip value
        #
        # Approximate USD account pip value
        # for a standard 1-lot position.
        # ----------------------------------

        if symbol.endswith("USD"):

            # EURUSD / GBPUSD / AUDUSD
            pip_value = 10.0

        elif symbol.startswith("USD"):

            # USDJPY
            #
            # Pip value in USD depends on
            # the current USDJPY price.
            #
            # For 1 standard lot:
            #
            # 100000 * 0.01 / price
            # --------------------------------

            pip_value = (

                100000
                * pip_size
                / entry

            )

        else:

            return None

        if pip_value <= 0:

            return None

        # ----------------------------------
        # Position size
        # ----------------------------------

        lot = self.sizer.calculate(

            balance,

            1,

            stop_loss_pips,

            pip_value

        )

        if lot <= 0:

            return None

        # ----------------------------------
        # Final risk package
        # ----------------------------------

        return {

            "lot": lot,

            "sl": sl,

            "tp": tp

        }
