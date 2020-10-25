import os
import sys
sys.path.append("..")

from . import races
from warrior import Warrior

class Race(Warrior):
    @staticmethod
    def get_races():
        return races.__all__

    @staticmethod
    def set_race(race):
        # load module
        module_name = "civilisations.races.{}".format(race)
        print(module_name)
        module = __import__ (module_name, fromlist=races.__all__)
        # initialize class
        return getattr(module, race.capitalize())()
