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

from analytics.statistics import Statistics

from services.notifications import NotificationService


class TradingEngine:

    def __init__(self):

        self.risk = RiskManager()

        self.orders = OrderManager()

        self.journal = TradeJournal()

        self.strategy = StrategyManager()

        self.stats = Statistics()

        self.notify = NotificationService()

        info("Trading Engine Initialized")

    def start(self):

        info("Engine Started")

        self.notify.send(
            "SYSTEM",
            "Nova-Trader-BM Started"
        )

    def analyse_market(self, data):

        signal = self.strategy.analyse(data)

        info(f"Signal: {signal}")

        return signal

    def execute(self):

        if self.risk.can_trade():

            info("Risk Check Passed")

        else:

            info("Trading Blocked")
