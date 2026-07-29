"""
==========================================
Trading Sessions
Nova-Trader-BM
==========================================
"""

from datetime import datetime


class TradingSession:

    def current(self):

        hour = datetime.utcnow().hour

        if 0 <= hour < 7:
            return "ASIAN"

        elif 7 <= hour < 13:
            return "LONDON"

        elif 13 <= hour < 22:
            return "NEW_YORK"

        return "CLOSED"
