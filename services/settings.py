"""
==========================================
Settings Service
Nova-Trader-BM
==========================================
"""

import json
import os


class Settings:

    FILE = "settings.json"

    def load(self):

        if not os.path.exists(self.FILE):

            return {}

        with open(self.FILE) as file:

            return json.load(file)

    def save(self, settings):

        with open(self.FILE, "w") as file:

            json.dump(

                settings,

                file,

                indent=4

            )
