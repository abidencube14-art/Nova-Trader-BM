"""
==========================================
Dashboard Data Provider
Nova-Trader-BM
==========================================
"""

from state.system_state import SystemState


system = SystemState()


class DashboardData:


    def get_status(self):

        return system.get()
