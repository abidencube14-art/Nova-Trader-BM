"""
==========================================
Helper Functions
Nova-Trader-BM
==========================================
"""


def percentage(value, percent):

    return value * (percent / 100)


def is_number(value):

    try:

        float(value)

        return True

    except:

        return False
