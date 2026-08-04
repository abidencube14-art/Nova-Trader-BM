"""
==========================================
Backtesting Engine
Nova-Trader-BM
==========================================
"""

from backtesting.statistics import Statistics

from backtesting.report import Report

from backtesting.equity_curve import EquityCurve


class BacktestingEngine:

    def __init__(self):

        self.stats = Statistics()

        self.report = Report()

        self.equity = EquityCurve()

    def run(

        self,

        trades

    ):

        statistics = self.stats.calculate(

            trades

        )

        curve = self.equity.build(

            trades

        )

        self.report.generate(

            statistics

        )

        return {

            "statistics": statistics,

            "equity": curve

        }
