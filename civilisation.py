from abc import ABC, abstractmethod
from map import Node

class Warrior(ABC):

    @property
    @abstractmethod
    def troops(self) -> int:
        pass

    @troops.setter
    @abstractmethod
    def troops(self, troops):
        pass

    @abstractmethod
    def end_turn(self):
        print("prout")

    @abstractmethod
    def authorizedterrain(self, node):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

class Civilisation(Warrior):
    def __init__(self, race, power, map):
        self.race = race
        self.power = power
        self.troops = race.troops + power.troops
        self.retreated = self.troops
        self.killed = 0
        self.declined = False
        self.map = map
        self.player = None

    def leave(self, node: Node):
        node.delete_defense_token(self.race.name)

    def setplayer(self, player):
        self.player = player

    def play(self):
        if not self.declined:
            self.gathertroops()
            self.attack()
            self.redeploy()
            self.end_turn()

    def gathertroops(self, *nodes):
        pass


    def occupiednodes(self, map):
        return map.occupiednodes(self.race.name)

    def end_turn(self) -> int:
        score = self.race.end_turn() + self.power.end_turn() + len(self.map.occupiedterritories())
        return score

    def authorizedterrain(self, node):
        return node["terrain"] != "sea"

    def canattack(self, node):
        if not(self.authorizedterrain(node[1])):
            print("This terrain is not attackable: {}".format(node[1]["terrain"]))
            return False
        if len(self.territories) == 0 and node[1]["border"]:
            pass
        elif not(node[0] in self.getneighbours()):
            print("Node #{} is not next to a territory you control".format(node[0]))
            return False
        if ("special" in node[1]):
            print("You cannot attack the node #{} because it is locked by {}.".format(node[0], node[1]["special"]))
            return False
        return True

    def gettokentoattack(self, node):
        token_needed = 2
        for key in node[1]["defense"]:
            token_needed += node[1]["defense"][key]
        return token_needed

    def attack(self, node):
        token_needed = self.gettokentoattack(node)
        if self.retreated >= token_needed:
            self.retreated -= token_needed
            self.territories.update({node[0], node[1]})
            return self.territories[node[0]]
        else:
            print("Not enough token to attack node #{}. You have {} token and you need {}")
        return token_needed

    def die(self, nodeid):
        if nodeid in self.territories:
            troops = self.territories[nodeid]["defense"][self.name]
            self.territories[nodeid]["defense"][self.name] = 0
            node = self.territories[nodeid]["defense"][self.name]
            troops -= 1
            self.retreated += troops
            return node
        else:
            print("Node #{} doesn't contain any {}s.".format(nodeid, self.name))
            return None



class Race(Warrior):
    pass

class Power(Warrior):
    pass

