"""
==========================================
Scheduler
Nova-Trader-BM
==========================================
"""

import time


class Scheduler:

    def __init__(self, interval=60):
        self.interval = interval

    def wait(self):
        time.sleep(self.interval)
