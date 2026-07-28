"""
==========================================
Nova-Trader-BM
==========================================
"""

from config import BOT_NAME, VERSION
from core.engine import TradingEngine
from core.logger import info


def banner():

    print("=" * 45)
    print(f"{BOT_NAME} v{VERSION}")
    print("=" * 45)


def main():

    banner()

    info("Loading Nova-Trader-BM...")

    engine = TradingEngine()

    engine.start()

    engine.analyse_market()

    engine.execute()

    info("Bot Ready.")


if __name__ == "__main__":
    main()
