"""
==========================================
Pipeline Steps
Nova-Trader-BM
==========================================
"""

class PipelineSteps:

    @staticmethod
    def market(context):

    candles = context["candles"]

    context["market_data"] = candles

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

    from strategy.manager import StrategyManager

    strategy = StrategyManager()

    context["signal"] = strategy.analyse(

        context["market_data"]

    )

    return context

    @staticmethod
def brain(context):

    from brain.brain import NovaBrain

    brain = NovaBrain()

    market = context.get("market", {})

    context["decision"] = brain.think(

        trend=market.get("trend", "SIDEWAYS"),

        indicators=context["indicators"],

        candle=context["market_data"].iloc[-1],

        support=market.get("support"),

        resistance=market.get("resistance"),

        volatility=market.get("volatility", "NORMAL")

    )

    return context

    @staticmethod
def risk(context):

    from risk.engine import RiskEngine

    engine = RiskEngine()

    atr = context["indicators"]["atr"]

    entry = context["market_data"].iloc[-1]["close"]

    context["risk"] = engine.evaluate(

        context["decision"].action,

        balance=10000,

        entry=entry,

        atr=atr

    )

    return context

    @staticmethod
def execution(context):

    from simulator.engine import SimulatorEngine

    simulator = SimulatorEngine()

    entry = context["market_data"].iloc[-1]["close"]

    trade = simulator.execute(

        symbol="EURUSD",

        decision=context["decision"],

        risk=context["risk"],

        entry=entry

    )

    context["trade"] = trade

    return context

    @staticmethod
def learning(context):

    if context.get("trade"):

        print("Learning from completed trade...")

    return context
