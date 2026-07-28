"""
==========================================
Notifications
Nova-Trader-BM
==========================================
"""

from core.logger import info


class NotificationService:

    def send(self, title, message):

        info(f"[{title}] {message}")
