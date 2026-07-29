"""
==========================================
Setup Memory
Nova-Trader-BM
==========================================
"""


class SetupMemory:

    def __init__(self):

        self.setups = []

    def remember(self, setup):

        self.setups.append(setup)

    def latest(self):

        if not self.setups:

            return None

        return self.setups[-1]

    def total(self):

        return len(self.setups)
