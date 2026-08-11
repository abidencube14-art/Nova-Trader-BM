"""
==========================================
Simulator Account
Nova-Trader-BM
==========================================
"""


class SimulatorAccount:

    def __init__(self, balance=10):

        self.initial_balance = balance

        self.balance = balance

        self.peak_balance = balance

        self.max_drawdown = 0.0

    def deposit(self, amount):

        self.balance += amount

        self._update_metrics()

    def withdraw(self, amount):

        self.balance -= amount

        self._update_metrics()

    def apply_profit_loss(self, amount):

        self.balance += amount

        self._update_metrics()

    def _update_metrics(self):

        if self.balance > self.peak_balance:

            self.peak_balance = self.balance

        drawdown = (
            self.peak_balance - self.balance
        )

        if drawdown > self.max_drawdown:

            self.max_drawdown = drawdown

    def get_balance(self):

        return self.balance

    def get_initial_balance(self):

        return self.initial_balance

    def get_peak_balance(self):

        return self.peak_balance

    def get_max_drawdown(self):

        return self.max_drawdown

    def get_return_percent(self):

        if self.initial_balance <= 0:

            return 0.0

        return round(

            (
                (self.balance - self.initial_balance)
                / self.initial_balance
            ) * 100,

            2

        )
