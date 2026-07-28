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


class TradingEngine:

    def __init__(self):

        self.risk = RiskManager()
        self.orders = OrderManager()
        self.journal = TradeJournal()

        info("Trading Engine Initialized")

    def start(self):

        info("Engine Started")

    def analyse_market(self):

        info("Analysing Market...")

    def execute(self):

        if self.risk.can_trade():

            info("Risk Check Passed")

        else:

            info("Trading Blocked By Risk Manager")
