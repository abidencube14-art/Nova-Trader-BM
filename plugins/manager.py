"""
==========================================
Plugin Manager
Nova-Trader-BM
==========================================
"""

from plugins.registry import PluginRegistry


class PluginManager:

    def __init__(self):

        self.registry = PluginRegistry()

    def register(self, plugin):

        self.registry.register(plugin)

    def enable_all(self):

        for plugin in self.registry.all():

            plugin.enable()

    def disable_all(self):

        for plugin in self.registry.all():

            plugin.disable()
