"""
==========================================
Order Manager
Nova-Trader-BM
==========================================
"""


class OrderManager:

    def __init__(self):

        self.active_orders = []

    def buy(self, symbol, lot):

        print(f"BUY {symbol} | Lot: {lot}")

    def sell(self, symbol, lot):

        print(f"SELL {symbol} | Lot: {lot}")

    def close(self, ticket):

        print(f"Closing Trade {ticket}")
