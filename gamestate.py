import random
import race

class GameState:
    def __init__(self):
        self.races = []
        self.round = []
        self.players = 2
        self.playerturn = 0
        self.racepool = []


    def shuffleraces(self):
        while(len(self.races)<6):
            random.randint(1, len(self.racepool))
    def start(self):
        shuffleraces()