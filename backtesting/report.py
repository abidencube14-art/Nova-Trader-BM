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

        closed_trades = history.closed_trades()

        open_trades = history.open_trades()

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

            f"{history.total_trades()}"

        )

        print(

            f"Closed Trades       : "

            f"{len(closed_trades)}"

        )

        print(

            f"Open Trades         : "

            f"{len(open_trades)}"

        )

        print(

            f"Winning Trades      : "

            f"{history.winning_trades()}"

        )

        print(

            f"Losing Trades       : "

            f"{history.losing_trades()}"

        )

        print(

            f"Win Rate            : "

            f"{history.win_rate()}%"

        )

        print()

        print("-----------------------------------")

        print("PROFITABILITY")

        print("-----------------------------------")

        print(

            f"Gross Profit        : "

            f"${history.gross_profit():.5f}"

        )

        print(

            f"Gross Loss          : "

            f"${history.gross_loss():.5f}"

        )

        print(

            f"Average Win         : "

            f"${history.average_win():.5f}"

        )

        print(

            f"Average Loss        : "

            f"${history.average_loss():.5f}"

        )

        print(

            f"Largest Win         : "

            f"${history.largest_win():.5f}"

        )

        print(

            f"Largest Loss        : "

            f"${history.largest_loss():.5f}"

        )

        print(

            f"Profit Factor       : "

            f"{history.profit_factor():.3f}"

        )

        print()

        print(

            f"Total P/L           : "

            f"${history.total_profit_loss():.2f}"

        )

        print("===================================")
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
