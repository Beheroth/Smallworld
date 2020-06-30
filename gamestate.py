import random
import race

class GameState:
    def __init__(self):
        self.races = []
        self.round = 0
        self.players = []
        self.playerturn = 0
        self.racepool = []

        self.controler = None


    def shuffleraces(self):
        while(len(self.races)<3):
            randindex = random.randint(0, len(self.racepool))
            self.races.append(self.racepool.pop(randindex))

    def start(self):
        self.shuffleraces()
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

