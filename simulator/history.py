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

    def closed_trades(self):

        return [

            trade

            for trade in self.trades

            if trade.status == "CLOSED"

        ]

    def open_trades(self):

        return [

            trade

            for trade in self.trades

            if trade.status == "OPEN"

        ]

    def total_trades(self):

        return len(self.trades)

    def winning_trades(self):

        return sum(

            1

            for trade in self.closed_trades()

            if trade.profit_loss > 0

        )

    def losing_trades(self):

        return sum(

            1

            for trade in self.closed_trades()

            if trade.profit_loss < 0

        )

    def total_profit_loss(self):

        return sum(

            trade.profit_loss

            for trade in self.closed_trades()

        )

    def win_rate(self):

        closed = len(self.closed_trades())

        if closed == 0:

            return 0.0

        return round(

            (

                self.winning_trades()

                / closed

            ) * 100,

            2

        )

    def gross_profit(self):

        return round(

            sum(

                trade.profit_loss

                for trade in self.closed_trades()

                if trade.profit_loss > 0

            ),

            5

        )

    def gross_loss(self):

        return round(

            abs(

                sum(

                    trade.profit_loss

                    for trade in self.closed_trades()

                    if trade.profit_loss < 0

                )

            ),

            5

        )

    def average_win(self):

        wins = [

            trade.profit_loss

            for trade in self.closed_trades()

            if trade.profit_loss > 0

        ]

        if not wins:

            return 0.0

        return round(

            sum(wins) / len(wins),

            5

        )

    def average_loss(self):

        losses = [

            trade.profit_loss

            for trade in self.closed_trades()

            if trade.profit_loss < 0

        ]

        if not losses:

            return 0.0

        return round(

            abs(sum(losses) / len(losses)),

            5

        )

    def largest_win(self):

        wins = [

            trade.profit_loss

            for trade in self.closed_trades()

            if trade.profit_loss > 0

        ]

        if not wins:

            return 0.0

        return round(

            max(wins),

            5

        )

    def largest_loss(self):

        losses = [

            trade.profit_loss

            for trade in self.closed_trades()

            if trade.profit_loss < 0

        ]

        if not losses:

            return 0.0

        return round(

            min(losses),

            5

        )

    def profit_factor(self):

        loss = self.gross_loss()

        if loss == 0:

            return 0.0

        return round(

            self.gross_profit() / loss,

            3

        )

    # ----------------------------------
    # Trade Efficiency
    # ----------------------------------

    def average_trade(self):

        closed = self.closed_trades()

        if not closed:

            return 0.0

        return round(

            self.total_profit_loss()
            / len(closed),

            5

        )

    def expectancy(self):

        closed = self.closed_trades()

        if not closed:

            return 0.0

        win_rate = (

            self.winning_trades()
            / len(closed)

        )

        loss_rate = (

            self.losing_trades()
            / len(closed)

        )

        expectancy = (

            win_rate * self.average_win()

            - loss_rate * self.average_loss()

        )

        return round(

            expectancy,

            5

        )

    # ----------------------------------
    # Direction Statistics
    # ----------------------------------

    def buy_trades(self):

        return sum(

            1

            for trade in self.trades

            if trade.action == "BUY"

        )

    def sell_trades(self):

        return sum(

            1

            for trade in self.trades

            if trade.action == "SELL"

        )

    # ----------------------------------
    # Winning Streak
    # ----------------------------------

    def longest_winning_streak(self):

        current = 0

        longest = 0

        for trade in self.closed_trades():

            if trade.profit_loss > 0:

                current += 1

                longest = max(

                    longest,

                    current

                )

            else:

                current = 0

        return longest

    # ----------------------------------
    # Losing Streak
    # ----------------------------------

    def longest_losing_streak(self):

        current = 0

        longest = 0

        for trade in self.closed_trades():

            if trade.profit_loss < 0:

                current += 1

                longest = max(

                    longest,

                    current

                )

            else:

                current = 0

        return longest
