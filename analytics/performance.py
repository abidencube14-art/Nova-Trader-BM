"""
==========================================
Performance Analytics
Nova-Trader-BM
==========================================
"""


class Performance:

    def __init__(self):

        self.total = 0
        self.wins = 0
        self.losses = 0

    def add_win(self):

        self.total += 1
        self.wins += 1

    def add_loss(self):

        self.total += 1
        self.losses += 1

    def win_rate(self):

        if self.total == 0:
            return 0

        return round(
            (self.wins / self.total) * 100,
            2
        )
