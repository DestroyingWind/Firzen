import numpy as np

from chess import *

class board():
    def __init__(self):
        self.base_board=np.zeros([20,20])
        self.player=[]
        self.rotate_flag=0

    def add_chess(self,position=(0,0),player_series=0,this_chess=chess()):
        shape=this_chess.chess.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                self.base_board[position[0]+i,position[1]+j]=player_series if this_chess.chess[i,j] else 0

    def rotate(self):
        self.base_board = np.rot90(self.base_board,-1)
        self.rotate_flag += 1
        self.rotate_flag %= 4

    def check_legal(self,position=(0,0),player_series=0,this_chess=chess()):
        pass