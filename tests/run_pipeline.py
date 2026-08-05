"""
==========================================
Pipeline Test
Nova-Trader-BM
==========================================
"""

import pandas as pd

from orchestrator.orchestrator import NovaOrchestrator


def load_sample_data():

    data = {

        "open": [

            1.1000,

            1.1010,

            1.1025,

            1.1030,

            1.1040,

            1.1050,

            1.1065,

            1.1075,

            1.1080,

            1.1090

        ],

        "high": [

            1.1010,

            1.1025,

            1.1035,

            1.1045,

            1.1055,

            1.1065,

            1.1075,

            1.1085,

            1.1095,

            1.1105

        ],

        "low": [

            1.0995,

            1.1005,

            1.1015,

            1.1025,

            1.1035,

            1.1045,

            1.1055,

            1.1065,

            1.1075,

            1.1085

        ],

        "close": [

            1.1008,

            1.1020,

            1.1030,

            1.1040,

            1.1050,

            1.1060,

            1.1070,

            1.1080,

            1.1090,

            1.1100

        ]

    }

    return pd.DataFrame(data)


def main():

    candles = load_sample_data()

    context = {

        "candles": candles

    }

    orchestrator = NovaOrchestrator()

    result = orchestrator.run(

        context

    )

    print("=" * 40)

    print("Nova-Trader-BM")

    print("=" * 40)

    print()

    print(result)


if __name__ == "__main__":

    main()
