import os

class Utils:
    def __init__(self):
        self.name = "Utils"

    @staticmethod
    def is_simulator():
        simulator = os.environ.get('SIMULATOR')
        if simulator != None and simulator == "1":
            return True
        return False