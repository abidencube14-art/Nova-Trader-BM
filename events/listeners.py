"""
==========================================
Default Event Listeners
Nova-Trader-BM
==========================================
"""

from core.logger import info


def on_market(payload):

    info(

        f"Market Updated: {payload}"

    )


def on_signal(payload):

    info(

        f"Signal: {payload}"

    )


def on_trade(payload):

    info(

        f"Trade: {payload}"

    )
