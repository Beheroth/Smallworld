class Race:
    def __init__(self, name, color, troops, power):
        self.name = name
        self.color = color
        self.power = power
        self.troops = troops + power.troops
        self.retreated = self.troops
        self.killed = 0
        self.declined = False
        self.territories = []

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

    def end_turn(self):
        return len(self.territories)


class Human(Race):
    def end_turn(self):
        points = super(Human, self).end_turn()
        for key in self.territories:
            if self.territories[key]["terrain"] == "field":
                points += 1
        return points

class Elf(Race):
    def die(self, nodeid):
        if nodeid in self.territories:
            troops = self.territories[nodeid]["defense"].pop(self.name)
            self.retreated += troops
            node = self.territories[nodeid]["defense"][self.name]
            return node
        else:
            print("Node #{} doesn't contain any {}.".format(nodeid, self.name))
            return None

class Halfling(Race):
    hole = 2

    def attack(self, node):
        token_needed = super(Halfling, self).attack(node)
        if self.hole > 0:
            self.territories[node[0]]["special"] = "Halfling"
            self.hole -= 1

    def canattack(self, node):
        if self.hole > 0:
            if not (self.authorizedterrain(node[1])):
                print("This terrain is not attackable: {}".format(node[1]["terrain"]))
                return False
            if ("special" in node[1]):
                print("You cannot attack the node #{} because it is locked by {}.".format(node[0], node[1]["special"]))
                return False
            return True
        else:
            return super(Halfling, self).canattack(node)


