"""
==========================================
Broker Adapter Base
Nova-Trader-BM
==========================================
"""

from abc import ABC, abstractmethod


class BrokerAdapter(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_positions(self):
        pass

    @abstractmethod
    def buy(self, symbol, lot, sl, tp):
        pass

    @abstractmethod
    def sell(self, symbol, lot, sl, tp):
        pass
