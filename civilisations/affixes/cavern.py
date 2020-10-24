from ..affix import Affix

class Cavern(Affix):
    def __init__(self):
        self.warriors_alive = 3
        self.warriors_dead = 0

    def get_warriors_alive(self):
        return self.warriors_alive

    def get_warriors_dead(self):
        return self.warriors_dead

    def get_warriors(self):
        return self.warriors_alive + self.warriors_dead

    def attack(self):
        pass

    def die(self):
        pass
