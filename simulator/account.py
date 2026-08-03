"""
==========================================
Simulator Account
Nova-Trader-BM
==========================================
"""


class SimulatorAccount:

    def __init__(self, balance=10000):

        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        self.balance -= amount

    def get_balance(self):

        return self.balance
