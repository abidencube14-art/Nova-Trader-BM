"""
==========================================
Trading Pipeline
Nova-Trader-BM
==========================================
"""

from logs.logger import NovaLogger


class TradingPipeline:

    def __init__(self):

        self.steps = []

        self.logger = NovaLogger()

    def add(self, step):

        self.steps.append(step)

    def run(self, context):

        for step in self.steps:

            self.logger.info(

                f"Running {step.__name__}"

            )

            context = step(context)

        self.logger.info(

            "Pipeline completed successfully."

        )

        return context
