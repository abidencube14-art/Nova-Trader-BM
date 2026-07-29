"""
==========================================
Optimisation Suggestions
Nova-Trader-BM
==========================================
"""

class Optimiser:

    def suggest(

        self,

        experience

    ):

        if experience["losses"] > experience["wins"]:

            return (

                "Strategy needs review."

            )

        return (

            "Strategy performing well."

        )
