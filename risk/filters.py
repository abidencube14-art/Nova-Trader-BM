"""
==========================================
Risk Filters
Nova-Trader-BM
==========================================
"""


class RiskFilters:

    def allow(self, signal):

        if signal is None:

            return False

        return signal.confidence >= 70
