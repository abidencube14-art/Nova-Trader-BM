"""
==========================================
Risk Filters
Nova-Trader-BM
==========================================
"""


class RiskFilters:

    def allow(

        self,

        signal

    ):

        return signal.confidence >= 70
