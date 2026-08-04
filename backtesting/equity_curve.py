"""
==========================================
Equity Curve
Nova-Trader-BM
==========================================
"""

class EquityCurve:

    def build(

        self,

        trades

    ):

        equity = []

        balance = 10000

        for trade in trades:

            balance += trade.profit

            equity.append(balance)

        return equity
