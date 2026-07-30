"""
==========================================
System Bootstrap
Nova-Trader-BM
==========================================
"""

from orchestrator.orchestrator import NovaOrchestrator

from orchestrator.context import TradingContext


def start():

    context = TradingContext()

    orchestrator = NovaOrchestrator()

    orchestrator.run(context)
