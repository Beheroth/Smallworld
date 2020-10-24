from random import randint
#from race import Race, Power
from map import Map
from abc import ABC, abstractmethod
from civilisation import Civilisation, Race, Power

class Strategy(ABC):
    @abstractmethod
    def pickciv(self, gamestate) -> int:
        pass

class User(Strategy):
    def __init__(self, player):
        self.player = player

    def pickciv(self, gamestate):
        min_index = 0
        min_value = None
        for i in range(len(gamestate.civilisations)):
            benef = gamestate.civilisations[i]["reward"] - i
            if not min_value or benef < min_value:
                min_value = benef
                min_index = i
        return min_index


class Player(object):
    def __init__(self, gamestate, strategy: Strategy):
        self.civilisations = []
        self.score = 5
        self.gamestate = gamestate
        self.strategy = strategy #AI or User

    def addciv(self, civilisation: Civilisation):
        civilisation.setplayer(self)
        self.civilisations.append(civilisation)

    def pickciv(self, index):
        self.score -= index
        civ = self.gamestate.withdrawciv(index=index)
        self.addciv(civ)

    def play(self):
        if self.civilisations[-1].declined:
            index = self.strategy.pickciv(self.gamestate)
            self.pickciv(index)
        for civ in self.civilisations:
            civ.play()

class GameState(object):
    def __init__(self, numberofplayers=2):
        self.map = Map(path='maps/{}players.json'.format(numberofplayers))
        self.racepool = self.loadracepool()
        self.powerpool = self.loadpowerpool()
        self.civilisations = []
        self.shuffleraces()
        self.round = 0
        self.players = [User(self) for i in range(numberofplayers)]
        self.playerturn = 0

    def loadracepool(self):
        return [Human()]

    def loadpowerpool(self):
        pass

    def shuffleraces(self):
        while(len(self.civilisations)<6):
            race = self.racepool.pop(randint(0, len(self.racepool)))
            power = self.powerpool.pop(randint(0, len(self.racepool)))
            self.civilisations.append({"civilisation": Civilisation(race, power, self.map), "reward":0})

    def withdrawciv(self, index):
        for i in range(index):
            self.civilisations[i]["reward"] += 1
        civ = self.civilisations.pop(index)
        self.shuffleraces()
        return civ

    def run(self):
        while(self.round < 10):
            while(self.playerturn < len(self.players)):
                self.players[self.playerturn].play()
                self.playerturn += 1
            self.playerturn = self.playerturn%len(self.players)
            self.round += 1
        print("The game has reached the end.")
        scores = []
        for player in self.players:
            print("{}: {}".format(player.name, player.getscore()))
            scores.append(player.getscore())
        print("{} wins the game with {}".format(self.players[scores.index(max(scores))].name, max(scores)))

