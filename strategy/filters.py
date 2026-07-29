"""
==========================================
Market Filters
Nova-Trader-BM
==========================================
"""


def volatility_filter(indicators):

    return indicators["atr"] > 0


def momentum_filter(indicators):

    return abs(indicators["histogram"]) > 0


def trade_allowed(indicators):

    return (

        volatility_filter(indicators)

        and

        momentum_filter(indicators)

    )
