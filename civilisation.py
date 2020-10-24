from abc import ABC, abstractmethod

class Warrior(ABC):
    @abstractmethod
    def __init__(self):
        self.warriors_alive = 0
        self.warriors_dead = 0

    @abstractmethod
    def get_warriors_alive(self):
        return self.warriors_alive

    @abstractmethod
    def get_warriors_dead(self):
        return self.warriors_dead

    @abstractmethod
    def get_warriors(self):
        return self.warriors_alive + self.warriors_dead

    @abstractmethod
    def attack(self, number_warriors, cell):
        return ("method attack to implement")

    @abstractmethod
    def die(self):
        return ("method die to implement")

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
        
