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

        if not self.filters.allow(decision):

            return None

        # ----------------------------------
        # Calculate direction-aware SL
        # ----------------------------------

        sl = self.sl.calculate(

            entry,

            atr,

            decision.action

        )

        # ----------------------------------
        # Calculate direction-aware TP
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
        # Pair-specific pip size
        # ----------------------------------

        if symbol.endswith("JPY"):

            pip_size = 0.01

        else:

            pip_size = 0.0001

        stop_loss_pips = (

            stop_distance / pip_size

        )

        # ----------------------------------
        # Pip value
        # ----------------------------------

        if symbol.endswith("JPY"):

            pip_value = 9.0

        else:

            pip_value = 10.0

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

        return {

            "lot": lot,

            "sl": sl,

            "tp": tp

        }
