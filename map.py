import json
from civilisation import Civilisation
from race import *

class Map(object):
    def __init__(self, path='maps/2players.json'):
        with open(path) as f:
            self._map = json.load(f)
            self.nodes = self._createnodes()

    def getnode(self, id):
        return self.nodes[id]

    def occupiednodes(self, race):
        nodes = []
        for id, node in self.nodes.items():
            if node.defense and len(node.defense) > 0:
                print("Ah, il y a de la défense")
                if race in node.defense.keys():
                    print("{} se trouve en {}".format(race, id))
                    nodes.append(id)
        return nodes

    def _createnodes(self):
        nodes = {}
        for key, value in self._map.items():
            node = Node(value)
            nodes[key] = node
        return nodes

class Node(object):
    def __init__(self, terrain, links, border=False, defense=None, markers=None, civilisation=None):
        self.terrain = terrain
        self.links = links
        self.border = border
        if defense:
            self.defense = defense
        if markers:
            self.markers = markers
        if civilisation:
            self.civilisation = civilisation

    @property
    def terrain(self):
        return self._terrain

    @terrain.setter
    def terrain(self, terrain):
        if terrain not in ["sea", "forest", "plain", "mountain", "swamp", "field"]:
            raise ValueError("{} is not a valid terrain type".format(terrain))
        else:
            self._terrain = terrain

    @property
    def civilisation(self):
        return self._civilisation

    @civilisation.setter
    def civilisation(self, civilisation: Civilisation):
        self._civilisation.leave(self)
        self._civilisation = civilisation
        self.defense[civilisation.name] = civilisation

    def isoccupiedby(self, race: str):
        if self.defense and race in self.defense.keys():
            return True
        return False

    def delete_defense_token(self, token_name):
        if self.defense and token_name in self.defense.keys():
            del self.defense[token_name]

    def gettotaldefense(self):
        total = 0
        for values in self.defense.values():
            total += values

    def __init__(self, d):
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                setattr(self, i,
                        self.obj_dic(i, j))
            elif isinstance(j, seqs):
                setattr(self, i,
                        type(j)(self.obj_dic(i, sj) if isinstance(sj, dict) else sj for sj in j))
            else:
                setattr(self, i, j)

    def obj_dic(self, name, d):
        top = type(name, (object,), d)
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                setattr(top, i, self.obj_dic(i, j))
            elif isinstance(j, seqs):
                setattr(top, i,
                        type(j)(self.obj_dic(i, sj) if isinstance(sj, dict) else sj for sj in j))
            else:
                setattr(top, i, j)
        return top


