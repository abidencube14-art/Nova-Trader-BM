"""
==========================================
Indicator Snapshot
Nova-Trader-BM
==========================================
"""

class IndicatorSnapshot:

    def __init__(self):

        self.values = {}

    def set(self, name, value):

        self.values[name] = value

    def get(self, name):

        return self.values.get(name)

    def all(self):

        return self.values
