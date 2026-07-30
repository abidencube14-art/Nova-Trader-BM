"""
==========================================
Plugin Base
Nova-Trader-BM
==========================================
"""

from abc import ABC, abstractmethod


class Plugin(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass
