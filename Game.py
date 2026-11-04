import random
import numpy as np

class Game:
    def __init__(self, n_horses):
        self.n_horses = n_horses
        self.pos = 0 # starting square for each horse
        self.home = False # if the horse is still at home -> pos_initial = 0

        ###############
        # GENERAL MAP #
        ###############

        self.house = 4 # number of horse_houses
        self.safe_square = 8
        self.lenght_map = 52 # distance between houses = 14
        
        self.map = np.zeros(self.lenght_map) # general map to take track of all horses 

        for s in self.house:
             self.map[1 + 14*s] = 1 # if the value is 1 it is a safe square
             self.map[9 + 14*s] = 1 # if the value is 1 it is a safe square
        
    def horse(self, Player):
        self.horse_dict = {}
        for ele_h in self.n_horses: 
             self.horse_dict[ele_h] = [Player, self.pos, self.home]
        
    def Ludo_1_player(self):
        pass
    def Ludo_2_players(self):
        pass
    def How_to_move(self):
            pass
