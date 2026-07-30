"""
==========================================
Nova Orchestrator
Nova-Trader-BM
==========================================
"""

from orchestrator.pipeline import TradingPipeline

from orchestrator.steps import PipelineSteps


class NovaOrchestrator:

    def __init__(self):

        self.pipeline = TradingPipeline()

        self.pipeline.add(PipelineSteps.market)

        self.pipeline.add(PipelineSteps.indicators)

        self.pipeline.add(PipelineSteps.strategy)

        self.pipeline.add(PipelineSteps.brain)

        self.pipeline.add(PipelineSteps.risk)

        self.pipeline.add(PipelineSteps.execution)

        self.pipeline.add(PipelineSteps.learning)

    def run(self, context):

        return self.pipeline.run(context)
