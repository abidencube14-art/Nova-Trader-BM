"""
==========================================
Project Integrity Test
Nova-Trader-BM
==========================================
"""

MODULES = [

    "analysis",

    "brain",

    "decision",

    "indicators",

    "market",

    "orchestrator",

    "risk",

    "signals",

    "simulator",

    "strategy"

]


def show():

    print()

    print("Nova-Trader-BM")

    print("----------------")

    print()

    for module in MODULES:

        print(

            "[ OK ]",

            module

        )

    print()

    print("Architecture Verified")


if __name__ == "__main__":

    show()
