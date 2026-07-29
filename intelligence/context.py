"""
==========================================
Market Context
Nova-Trader-BM
==========================================
"""


class MarketContext:

    def build(

        self,

        session,

        trend,

        confidence,

        score

    ):

        return {

            "session": session,

            "trend": trend,

            "confidence": confidence,

            "score": score

        }
