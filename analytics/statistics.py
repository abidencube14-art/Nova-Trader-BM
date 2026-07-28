"""
==========================================
Statistics
Nova-Trader-BM
==========================================
"""

class Statistics:

    def __init__(self):

        self.total_trades = 0
        self.winning_trades = 0
        self.losing_trades = 0
        self.total_profit = 0.0

    def record_trade(self, profit):

        self.total_trades += 1

        self.total_profit += profit

        if profit >= 0:
            self.winning_trades += 1
        else:
            self.losing_trades += 1

    def win_rate(self):

        if self.total_trades == 0:
            return 0

        return round(
            (self.winning_trades /
             self.total_trades) * 100,
            2
        )

    def summary(self):

        return {

            "Trades": self.total_trades,

            "Wins": self.winning_trades,

            "Losses": self.losing_trades,

            "Win Rate": self.win_rate(),

            "Profit": self.total_profit

        }
