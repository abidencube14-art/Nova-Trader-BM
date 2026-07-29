"""
==========================================
Health Monitor
Nova-Trader-BM
==========================================
"""


class HealthMonitor:

    def __init__(self):

        self.status = {
            "engine": True,
            "market": True,
            "strategy": True,
            "risk": True,
            "broker": False
        }

    def update(self, module, state):

        self.status[module] = state

    def healthy(self):

        return all(self.status.values())

    def report(self):

        return self.status
