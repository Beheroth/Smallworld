from civilisation import Race

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

class Indigen(Race):
    pass


