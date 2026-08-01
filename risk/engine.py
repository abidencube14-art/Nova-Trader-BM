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

        signal,

        balance,

        entry,

        atr

    ):

        if not self.filters.allow(signal):

            return None

        lot = self.sizer.calculate(

            balance,

            1,

            20,

            10

        )

        return {

            "lot": lot,

            "sl": self.sl.calculate(

                entry,

                atr

            ),

            "tp": self.tp.calculate(

                entry,

                atr

            )

        }
