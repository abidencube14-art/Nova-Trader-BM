"""
==========================================
Emergency Manager
Nova-Trader-BM
==========================================
"""


class EmergencyManager:

    def should_stop(

        self,

        daily_loss,

        max_loss

    ):

        return daily_loss >= max_loss
