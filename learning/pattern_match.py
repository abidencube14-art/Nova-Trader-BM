"""
==========================================
Pattern Matching
Nova-Trader-BM
==========================================
"""


class PatternMatcher:

    def compare(

        self,

        current,

        previous

    ):

        score = 0

        for key in current:

            if key in previous:

                if current[key] == previous[key]:

                    score += 1

        return score
