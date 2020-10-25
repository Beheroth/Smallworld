from civilisations.race import Race
from civilisations.affix import Affix
from warrior import Warrior

class Civilisation(Warrior):
    def __init__(self, race, affix):
        self.race = race
        self.affix = affix
        self.warriors_alive = race.get_warriors_alive() + affix.get_warriors_alive()
        self.warriors_dead = race.get_warriors_dead() + affix.get_warriors_dead()

    def get_warriors_alive(self):
        pass
    
    def get_warriors_dead(self):
        pass

    def get_warriors(self):
        pass

    def attack(self):
        self.race.attack()
        self.affix.attack()

    def die(self):
        self.race.die()
        self.affix.die()
        
    @staticmethod
    def get_races_and_affixes():
        races = Race.get_races()
        affixes = Affix.get_affixes()
        return races, affixes
