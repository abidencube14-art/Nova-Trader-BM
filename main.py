"""
==========================================
Nova-Trader-BM
Version 1.0.0
==========================================
"""

from config import BOT_NAME, VERSION

def banner():

    print("=" * 45)
    print(f"{BOT_NAME}  v{VERSION}")
    print("=" * 45)
    print("Starting bot...")
    print()

def main():

    banner()

    print("Loading configuration...")

    print("Configuration Loaded.")

    print()

    print("Waiting for MT5 connection...")

if __name__ == "__main__":
    main()
