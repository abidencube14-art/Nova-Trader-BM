"""
==========================================
Nova-Trader-BM Configuration
==========================================
Edit this file to customise the bot.
"""

# =========================
# MetaTrader 5
# =========================

MT5_LOGIN = 0
MT5_PASSWORD = ""
MT5_SERVER = ""

# =========================
# Trading
# =========================

SYMBOL = "EURUSD"

TIMEFRAME = "M15"

LOT_SIZE = 0.01

STOP_LOSS = 300

TAKE_PROFIT = 600

MAGIC_NUMBER = 987654

# =========================
# Risk Management
# =========================

RISK_PER_TRADE = 1.0

MAX_OPEN_TRADES = 2

MAX_DAILY_LOSS = 3.0

# =========================
# Indicators
# =========================

EMA_FAST = 50

EMA_SLOW = 200

RSI_PERIOD = 14

ATR_PERIOD = 14

# =========================
# Bot
# =========================

BOT_NAME = "Nova-Trader-BM"

VERSION = "1.0.0"
