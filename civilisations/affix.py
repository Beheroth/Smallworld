import os
import sys
sys.path.append("..")

from . import affixes
from civilisation import Warrior

class Affix(Warrior):
    @staticmethod
    def get_affix():
        return affixes.__all__

    @staticmethod
    def set_affix(affix):
        # load module
        module_name = "civilisations.affixes.{}".format(affix)
        module = __import__ (module_name, fromlist=affixes.__all__)
        # initialize class
        return getattr(module, affix.capitalize())()
