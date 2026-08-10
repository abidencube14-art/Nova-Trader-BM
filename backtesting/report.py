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

        print()

        print("===================================")

        print("NOVA BACKTEST REPORT")

        print("===================================")

        print(

            f"Starting Balance : $10.00"

        )

        print(

            f"Ending Balance   : "

            f"${account.get_balance():.2f}"

        )

        print(

            f"Total Trades     : "

            f"{history.total_trades()}"

        )

        print(

            f"Winning Trades   : "

            f"{history.winning_trades()}"

        )

        print(

            f"Losing Trades    : "

            f"{history.losing_trades()}"

        )

        print(

            f"Win Rate         : "

            f"{history.win_rate()}%"

        )

        print(

            f"Total P/L        : "

            f"${history.total_profit_loss():.2f}"

        )

        print("===================================")
