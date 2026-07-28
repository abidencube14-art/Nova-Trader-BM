"""
==========================================
Risk Manager
Nova-Trader-BM
==========================================
"""

from config import (
    RISK_PER_TRADE,
    MAX_OPEN_TRADES,
    MAX_DAILY_LOSS
)


class RiskManager:

    def __init__(self):

        self.daily_loss = 0
        self.open_trades = 0

    def can_trade(self):

        if self.open_trades >= MAX_OPEN_TRADES:
            return False

        if self.daily_loss >= MAX_DAILY_LOSS:
            return False

        return True

    def add_trade(self):

        self.open_trades += 1

    def close_trade(self):

        if self.open_trades > 0:
            self.open_trades -= 1

    def add_loss(self, percent):

        self.daily_loss += percent
