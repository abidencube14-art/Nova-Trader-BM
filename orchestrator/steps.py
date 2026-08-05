"""
==========================================
Pipeline Steps
Nova-Trader-BM
==========================================
"""

class PipelineSteps:

    @staticmethod
def market(context):

    context["market_data"] = context["candles"]

    return context

    @staticmethod
def indicators(context):

    from indicators.manager import IndicatorManager

    manager = IndicatorManager()

    context["indicators"] = manager.analyse(

        context["market_data"]

    )

    return context
    
    @staticmethod
def strategy(context):

    from analysis.engine import AnalysisEngine

    analysis = AnalysisEngine()

    context["market"] = analysis.analyse(

        context["market_data"],

        context["indicators"]

    )

    return context

    @staticmethod
def brain(context):

    from brain.brain import NovaBrain

    brain = NovaBrain()

    market = context["market"]

    context["decision"] = brain.think(

        trend=market["trend"],

        indicators=context["indicators"],

        candle=context["market_data"].iloc[-1],

        support=market["support"],

        resistance=market["resistance"],

        volatility=market["volatility"]

    )

    return context

    @staticmethod
def risk(context):

    context["risk"] = context["decision"].risk

    return context

    @staticmethod
def execution(context):

    from simulator.engine import SimulatorEngine

    simulator = SimulatorEngine()

    entry = context["market_data"].iloc[-1]["close"]

    context["trade"] = simulator.execute(

        symbol="EURUSD",

        decision=context["decision"],

        risk=context["risk"],

        entry=entry

    )

    return context

    @staticmethod
def learning(context):

    if context["trade"] is not None:

        print(

            "Learning from",

            context["trade"].symbol

        )

    return context
