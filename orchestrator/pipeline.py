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

    from logs.errors import ErrorHandler

    for step in self.steps:

        try:

            self.logger.info(

                f"Running {step.__name__}"

            )

            context = step(context)

        except Exception as e:

            ErrorHandler.handle(e)

            break

    return context
