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

        balance,

        entry,

        atr

    ):

        if not self.filters.allow(decision):

            return None

        # ----------------------------------
        # Calculate Stop Loss
        # ----------------------------------

        sl = self.sl.calculate(

            entry,

            atr

        )

        # ----------------------------------
        # Calculate Take Profit
        # ----------------------------------

        tp = self.tp.calculate(

            entry,

            atr

        )

        # ----------------------------------
        # Calculate actual stop distance
        # ----------------------------------

        stop_distance = abs(

            entry - sl

        )

        # ----------------------------------
        # Convert price distance to pips
        # ----------------------------------

        stop_loss_pips = stop_distance * 10000

        if stop_loss_pips <= 0:

            return None

        # ----------------------------------
        # Standard pip value
        # ----------------------------------

        pip_value = 10

        # ----------------------------------
        # Position size
        # ----------------------------------

        lot = self.sizer.calculate(

            balance,

            1,

            stop_loss_pips,

            pip_value

        )

        return {

            "lot": lot,

            "sl": sl,

            "tp": tp

        }
