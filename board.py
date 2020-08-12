import numpy as np

class board():
    def __init__(self):
        self.base_board=np.zeros([20,20])
        self.player=[]

    def add_player(self,player):
        if self.player.__len__()<3:
            self.player.append(player)
            return True,len(self.player)
        