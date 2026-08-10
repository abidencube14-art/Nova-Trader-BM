"""
==========================================
Backtest Report
Nova-Trader-BM
==========================================
"""


class Report:

    def generate(

        self,

        simulator

    ):

        history = simulator.history

        account = simulator.account

        trades = history.all()

        closed_trades = [

            trade

            for trade in trades

            if trade.status == "CLOSED"

        ]

        open_trades = [

            trade

            for trade in trades

            if trade.status == "OPEN"

        ]

        winning_trades = sum(

            1

            for trade in closed_trades

            if trade.profit_loss > 0

        )

        losing_trades = sum(

            1

            for trade in closed_trades

            if trade.profit_loss < 0

        )

        closed_count = len(closed_trades)

        if closed_count > 0:

            win_rate = round(

                (winning_trades / closed_count) * 100,

                2

            )

        else:

            win_rate = 0.0

        total_profit_loss = sum(

            trade.profit_loss

            for trade in closed_trades

        )

        print()

        print("===================================")

        print("NOVA BACKTEST REPORT")

        print("===================================")

        print(

            "Starting Balance : $10.00"

        )

        print(

            f"Ending Balance   : "

            f"${account.get_balance():.2f}"

        )

        print(

            f"Total Trades Opened : "

            f"{len(trades)}"

        )

        print(

            f"Closed Trades       : "

            f"{closed_count}"

        )

        print(

            f"Open Trades         : "

            f"{len(open_trades)}"

        )

        print(

            f"Winning Trades      : "

            f"{winning_trades}"

        )

        print(

            f"Losing Trades       : "

            f"{losing_trades}"

        )

        print(

            f"Win Rate            : "

            f"{win_rate}%"

        )

        print(

            f"Total P/L           : "

            f"${total_profit_loss:.2f}"

        )

        print("===================================")
