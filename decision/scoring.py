"""
==========================================
Decision Scoring System
Nova-Trader-BM
==========================================
"""

class DecisionScore:

    def __init__(self):

        self.score = 0

        self.details = {}

    def add(self, name, points):

        self.details[name] = points

        self.score += points

    def total(self):

        return self.score

    def report(self):

        return self.details
