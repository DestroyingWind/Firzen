from board import *
from game import *
import torch
from nn_model import identicle__nn


class Agent:
    def __init__(self, learning_rate=0.1, epsilon=0.05):
        self.lr = learning_rate
        self.epsilon = epsilon
        self.nn = identicle__nn()

    def choose_action(self, board: Board, policy_set):
        values = []
        for eachpolicy in policy_set:
            value = self.value_function(board, eachpolicy)
            values.append(value)
        rand = random.random()
        if rand < self.epsilon:
            select_num = random.randint(0, values.__len__() - 1)
        else:
            select_num = np.argmax(np.array(values))
        return select_num

    def value_function(self, board: np.array, action: np.array):
        # todo build nn for value function
        before=board.base_board.copy()
        this_chess = chesses[action[0]]
        this_chess.change_to(reverse_times=action[1], rotate_times=action[2])
        board.add_chess(position=(action[3], action[4]), player_series=0, this_chess=this_chess)
        after=board.base_board.copy()
        in_tensor = self.board_to_tensor(before,after)
        score = self.nn(in_tensor)
        board.remove_chess(position=(action[3], action[4]), this_chess=this_chess)
        this_chess.reset()
        return score

    def board_to_tensor(self, board: np.array, action: np.array):
        before = board.copy()
        after = action.copy()
        before += np.ones([BOARD_SIZE, BOARD_SIZE])
        after += np.ones([BOARD_SIZE, BOARD_SIZE])
        tensor_before = torch.tensor(before, dtype=torch.float)
        tensor_after = torch.tensor(after, dtype=torch.float)
        t0=torch.tensor(np.zeros([BOARD_SIZE,BOARD_SIZE]),dtype=torch.float)
        t1=torch.tensor(np.ones([BOARD_SIZE,BOARD_SIZE]),dtype=torch.float)
        tb0=torch.where(tensor_before == 1,t1,t0)
        tb1=torch.where(tensor_before == 2,t1,t0)
        tb2=torch.where(tensor_before == 3,t1,t0)
        tb3=torch.where(tensor_before == 4, t1, t0)
        ta0=torch.where(tensor_after == 1,t1,t0)
        ta1=torch.where(tensor_after == 2,t1,t0)
        ta2=torch.where(tensor_after == 3,t1,t0)
        ta3=torch.where(tensor_after == 4,t1,t0)
        out_tensor=torch.stack([tb0,tb1,tb2,tb3,ta0,ta1,ta2,ta3],dim=0)
        out_tensor=torch.unsqueeze(out_tensor,0)
        print(out_tensor.shape)
        return out_tensor

if __name__=="__main__":
    a=Agent()
    b=a.board_to_tensor(np.random.random([BOARD_SIZE,BOARD_SIZE]),np.random.random([BOARD_SIZE,BOARD_SIZE]))
    print(b)