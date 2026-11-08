import random
import numpy as np

class Game:
    def __init__(self, n_horses = int, n_players = int) -> None:
        self.n_horses = n_horses
        self.n_players = n_players

        self.pos = 0 # starting square for each horse
        self.home = False # if the horse is still at home -> pos_initial = 0
        self.house = 4 # number of horse_houses
        self.lenght_map = 52 # distance between houses = 14
        self.safe_square = 8 # number of safe squares 
        
        ###############
        # GENERAL MAP #
        ###############
        
        # -> [array, bool]
        self.map = [] # array with first entry an array -> how many horses are in square s, second entry -> safe_sq

        for m in self.lenght_map:
             self.map.append([np.zeros(self.n_horses), False]) # useful because we can sum of each square to know if are horses

        for s in self.house:
            self.map[1 + 14*s] = [np.zeros(self.n_horses * self.n_players), True] # I expand the number of possible horses in a safesquare 
            self.map[9 + 14*s] = [np.zeros(self.n_horses * self.n_players), True] # I expand the number of possible horses in a safesquare 
        
        # example if a turn T there are four horses in safesquare s [[1,1,2,2], True]
        
    def horses(self, Player = int) -> dict:
        self.horses_dict = {}
        for ele_h in self.n_horses: 
             self.horsea_dict[ele_h] = [Player, self.pos, self.home]

        return self.horses_dict
        
    def Ludo_1_player(self):
        pass

    def Ludo_2_players(self):
        pass

    def Global_postion(self, Player = int, position = int) -> int: # function that gives the exact position on the map, must not be at home
        real_postion = (Player - 1) * 14 + position
        if real_postion > self.lenght_map:
            return real_postion - self.lenght_map
        else:
            return real_postion


