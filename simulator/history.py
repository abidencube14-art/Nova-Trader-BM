"""
==========================================
Trade History
Nova-Trader-BM
==========================================
"""


class TradeHistory:

    def __init__(self):

        self.trades = []

    def add(self, trade):

        self.trades.append(trade)

    def all(self):

        return self.trades

    def total_trades(self):

        return len(self.trades)

    def winning_trades(self):

        return sum(

            1

            for trade in self.trades

            if trade.status == "CLOSED"

            and trade.profit_loss > 0

        )

    def losing_trades(self):

        return sum(

            1

            for trade in self.trades

            if trade.status == "CLOSED"

            and trade.profit_loss < 0

        )

    def total_profit_loss(self):

        return sum(

            trade.profit_loss

            for trade in self.trades

            if trade.status == "CLOSED"

        )

    def win_rate(self):

        closed = (

            self.winning_trades()

            + self.losing_trades()

        )

        if closed == 0:

            return 0.0

        return round(

            (

                self.winning_trades()

                / closed

            ) * 100,

            2

        )
