"""
==========================================
Trading Engine
Nova-Trader-BM
==========================================
"""

from core.logger import info

from risk.risk_manager import RiskManager

from broker.orders import OrderManager

from journal.trades import TradeJournal

from strategy.manager import StrategyManager


class TradingEngine:

    def __init__(self):

        self.risk = RiskManager()

        self.orders = OrderManager()

        self.journal = TradeJournal()

        self.strategy = StrategyManager()

        info("Trading Engine Initialized")

    def start(self):

        info("Engine Started")

        info(f"Strategy: {self.strategy.current_strategy()}")

    def analyse_market(self, data):

        signal = self.strategy.analyse(data)

        info(f"Signal: {signal}")

        return signal

    def execute(self):

        if self.risk.can_trade():

            info("Risk Check Passed")

        else:

            info("Risk Manager Blocked Trading")
