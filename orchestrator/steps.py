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

        return context

    @staticmethod
    def risk(context):

        return context

    @staticmethod
    def execution(context):

        return context

    @staticmethod
    def learning(context):

        return context
