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

        print()

        print("===================================")
        print("NOVA BACKTEST REPORT")
        print("===================================")

        print(
            f"Starting Balance : $10.00"
        )

        print(
            f"Ending Balance   : ${balance:.2f}"
        )

        print(
            f"Total Trades Opened : {total_trades}"
        )

        print(
            f"Closed Trades       : {closed_trades}"
        )

        print(
            f"Open Trades         : {open_trades}"
        )

        print(
            f"Winning Trades      : {winning_trades}"
        )

        print(
            f"Losing Trades       : {losing_trades}"
        )

        print(
            f"Win Rate            : {win_rate}%"
        )

        print()

        print("-----------------------------------")
        print("PROFITABILITY")
        print("-----------------------------------")

        print(
            f"Gross Profit        : ${gross_profit:.5f}"
        )

        print(
            f"Gross Loss          : ${gross_loss:.5f}"
        )

        print(
            f"Average Win         : ${average_win:.5f}"
        )

        print(
            f"Average Loss        : ${average_loss:.5f}"
        )

        print(
            f"Largest Win         : ${largest_win:.5f}"
        )

        print(
            f"Largest Loss        : ${largest_loss:.5f}"
        )

        print(
            f"Profit Factor       : {profit_factor:.3f}"
        )

        print()

        print(
            f"Total P/L           : ${total_profit_loss:.2f}"
        )

        print("===================================")
