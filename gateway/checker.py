"""
==========================================
Platform Checker
Nova-Trader-BM
==========================================
"""

from gateway.platforms import SUPPORTED_PLATFORMS


class PlatformChecker:

    def supported(

        self,

        platform

    ):

        return platform in SUPPORTED_PLATFORMS
