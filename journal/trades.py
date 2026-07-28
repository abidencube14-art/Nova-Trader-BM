"""
==========================================
Trade Journal
Nova-Trader-BM
==========================================
"""

import csv
import os


FILE = "journal/trades.csv"


class TradeJournal:

    def __init__(self):

        if not os.path.exists(FILE):

            with open(FILE, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Time",
                    "Pair",
                    "Direction",
                    "Entry",
                    "Exit",
                    "Profit"
                ])

    def record(
        self,
        time,
        pair,
        direction,
        entry,
        exit_price,
        profit
    ):

        with open(FILE, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                time,
                pair,
                direction,
                entry,
                exit_price,
                profit
            ])
