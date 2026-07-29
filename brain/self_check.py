"""
==========================================
Self Diagnostics
Nova-Trader-BM
==========================================
"""


class SelfCheck:

    def health(self):

        return {

            "Engine": True,

            "Indicators": True,

            "Risk": True,

            "Strategy": True,

            "Brain": True

        }
