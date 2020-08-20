from board import *
from game import *


class Agent:
    def __init__(self,learning_rate=0.1,epsilon=0.05):
        self.lr=learning_rate
        self.epsilon=epsilon

    def choose_action(self,board:Board,policy_set):
        for eachpolicy in policy_set:
            value=self.value_function(board,eachpolicy)

    def value_function(self, board: Board,action):
        return np.sum(board.base_board)
