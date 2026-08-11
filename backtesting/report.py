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
        # Trade statistics
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

        # ----------------------------------
        # Profitability statistics
        # ----------------------------------

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

        # ----------------------------------
        # Account statistics
        # ----------------------------------

        starting_balance = (
            account.get_initial_balance()
        )

        balance = (
            account.get_balance()
        )

        peak_balance = (
            account.get_peak_balance()
        )

        max_drawdown = (
            account.get_max_drawdown()
        )

        return_percent = (
            account.get_return_percent()
        )

        if peak_balance > 0:

            drawdown_percent = round(

                (
                    max_drawdown
                    / peak_balance
                ) * 100,

                2

            )

        else:

            drawdown_percent = 0.0

        # ----------------------------------
        # Report
        # ----------------------------------

        print()

        print("===================================")
        print("NOVA BACKTEST REPORT")
        print("===================================")

        print(
            f"Starting Balance : "
            f"${starting_balance:.2f}"
        )

        print(
            f"Ending Balance   : "
            f"${balance:.2f}"
        )

        print(
            f"Return           : "
            f"{return_percent:.2f}%"
        )

        print(
            f"Peak Balance     : "
            f"${peak_balance:.2f}"
        )

        print(
            f"Max Drawdown     : "
            f"${max_drawdown:.2f}"
        )

        print(
            f"Drawdown %       : "
            f"{drawdown_percent:.2f}%"
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

        print("===================================")
