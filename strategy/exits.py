"""
==========================================
Trade Exit Logic
Nova-Trader-BM
==========================================
"""


def exit_signal(position, current_price, stop_loss, take_profit):

    if position == "BUY":

        if current_price <= stop_loss:
            return "STOP_LOSS"

        if current_price >= take_profit:
            return "TAKE_PROFIT"

    elif position == "SELL":

        if current_price >= stop_loss:
            return "STOP_LOSS"

        if current_price <= take_profit:
            return "TAKE_PROFIT"

    return "HOLD"
