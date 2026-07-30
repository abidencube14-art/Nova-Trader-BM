"""
==========================================
MT5 Connection
Nova-Trader-BM
==========================================
"""

class MT5Connection:

    def __init__(self):

        self.connected = False

    def connect(self):

        print("Connecting to MT5...")

        self.connected = True

        return self.connected

    def disconnect(self):

        self.connected = False

    def status(self):

        return self.connected
