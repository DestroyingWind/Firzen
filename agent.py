from board import *
from game import *


class Agent:
    def __init__(self,learning_rate=0.1,epsilon=0.05):
        self.lr=learning_rate
        self.epsilon=epsilon

    def choose_action(self,board:Board,policy_set):
        values=[]
        for eachpolicy in policy_set:
            value=self.value_function(board,eachpolicy)
            values.append(value)
        rand=random.random()
        if rand<self.epsilon:
            select_num=random.randint(0,values.__len__()-1)
        else:
            select_num=np.argmax(np.array(values))
        return select_num

    def value_function(self, board: Board,action):
        # todo build nn for value function
        return np.sum(board.base_board)
