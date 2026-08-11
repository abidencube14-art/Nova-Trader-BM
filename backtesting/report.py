"""
==========================================
Backtest Report
Nova-Trader-BM
==========================================
"""


class Report:

    def generate(self, simulator):

        history = simulator.history

        account = simulator.account

        # ----------------------------------
        # Statistics
        # ----------------------------------

        total_trades = history.total_trades()

        closed_trades = len(
            history.closed_trades()
        )

        open_trades = len(
            history.open_trades()
        )

        winning_trades = history.winning_trades()

        losing_trades = history.losing_trades()

        win_rate = history.win_rate()

        gross_profit = history.gross_profit()

        gross_loss = history.gross_loss()

        average_win = history.average_win()

        average_loss = history.average_loss()

        largest_win = history.largest_win()

        largest_loss = history.largest_loss()

        profit_factor = history.profit_factor()

        total_profit_loss = (
            history.total_profit_loss()
        )

        balance = account.get_balance()

        # ----------------------------------
        # Report
        # ----------------------------------

        print()

        print("===================================")

        print("NOVA BACKTEST REPORT")

        print("===================================")

        print(
            "Starting Balance : $10.00"
        )

        print(
            f"Ending Balance   : "
            f"${balance:.2f}"
        )

        print(
            f"Total Trades Opened : "
            f"{total_trades}"
        )

        print(
            f"Closed Trades       : "
            f"{closed_trades}"
        )

        print(
            f"Open Trades         : "
            f"{open_trades}"
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

        print()

        print("-----------------------------------")

        print("PROFITABILITY")

        print("-----------------------------------")

        print(
            f"Gross Profit        : "
            f"${gross_profit:.5f}"
        )

        print(
            f"Gross Loss          : "
            f"${gross_loss:.5f}"
        )

        print(
            f"Average Win         : "
            f"${average_win:.5f}"
        )

        print(
            f"Average Loss        : "
            f"${average_loss:.5f}"
        )

        print(
            f"Largest Win         : "
            f"${largest_win:.5f}"
        )

        print(
            f"Largest Loss        : "
            f"${largest_loss:.5f}"
        )

        print(
            f"Profit Factor       : "
            f"{profit_factor:.3f}"
        )

        print()

        print(
            f"Total P/L           : "
            f"${total_profit_loss:.2f}"
        )

        print("===================================")        print("-----------------------------------")

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
