"""
==========================================
Storage
Nova-Trader-BM
==========================================
"""

import json
import os


class Storage:

    def save(self, filename, data):

        with open(filename, "w") as file:

            json.dump(data, file, indent=4)

    def load(self, filename):

        if not os.path.exists(filename):

            return {}

        with open(filename) as file:

            return json.load(file)
