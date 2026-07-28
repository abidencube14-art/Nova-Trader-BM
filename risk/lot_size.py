"""
==========================================
Lot Size Calculator
Nova-Trader-BM
==========================================
"""


def calculate_lot_size(
    balance,
    risk_percent,
    stop_loss_pips,
    pip_value=10
):

    risk_amount = balance * (risk_percent / 100)

    lot_size = risk_amount / (stop_loss_pips * pip_value)

    return round(lot_size, 2)
