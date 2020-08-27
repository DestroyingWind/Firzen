from board import *
import torch
import nn_model
import random
import numpy as np
import chess

Gamma=0.9
Alpha=0.5

class Agent:
    def __init__(self, epsilon=0.05,model=nn_model.Identicle_nn()):
        self.epsilon = epsilon
        self.nn = model

    def choose_action(self, board: Board, policy_set):
        values = []
        rand = random.random()
        if rand <= self.epsilon:
            select_num = random.randint(0, policy_set.__len__() - 1)
            return select_num,self.value_function(board,policy_set[select_num])
        else:
            for eachpolicy in policy_set:
                value = self.value_function(board, eachpolicy)
                values.append(value)
            select_num = int(np.argmax(np.array(values)))
            return select_num, values[select_num]

    def value_function(self, board: Board, action=(0,0,0,0,0)):
        # todo build nn for value function
        before=board.base_board.astype(np.float64)
        this_chess = chess.chesses[action[0]]
        this_chess.change_to(reverse_times=action[1], rotate_times=action[2])
        board.add_chess(position=(action[3], action[4]), player_series=0, this_chess=this_chess)
        after=board.base_board.astype(np.float64)
        in_tensor = self.board_to_tensor(before,after)
        in_tensor=torch.unsqueeze(in_tensor,0)
        score = self.nn(in_tensor)
        board.remove_chess(position=(action[3], action[4]), this_chess=this_chess)
        this_chess.reset()
        return score

    @staticmethod
    def board_to_tensor(board: np.array, action: np.array):
        before = board.copy()
        after = action.copy()
        if not before.dtype==np.float64:
            before=before.astype(np.float64)
        if not after.dtype==np.float64:
            after=after.astype(np.float64)
        # print(before.dtype)
        before += np.ones([BOARD_SIZE, BOARD_SIZE],dtype=np.float)
        after += np.ones([BOARD_SIZE, BOARD_SIZE],dtype=np.float)
        tensor_before = torch.tensor(before, dtype=torch.float,device=nn_model.device)
        tensor_after = torch.tensor(after, dtype=torch.float,device=nn_model.device)
        t0=torch.tensor(np.zeros([BOARD_SIZE,BOARD_SIZE]),dtype=torch.float,device=nn_model.device)
        t1=torch.tensor(np.ones([BOARD_SIZE,BOARD_SIZE]),dtype=torch.float,device=nn_model.device)
        tb0=torch.where(tensor_before == 1,t1,t0)
        tb1=torch.where(tensor_before == 2,t1,t0)
        tb2=torch.where(tensor_before == 3,t1,t0)
        tb3=torch.where(tensor_before == 4, t1, t0)
        ta0=torch.where(tensor_after == 1,t1,t0)
        ta1=torch.where(tensor_after == 2,t1,t0)
        ta2=torch.where(tensor_after == 3,t1,t0)
        ta3=torch.where(tensor_after == 4,t1,t0)
        out_tensor=torch.stack([tb0,tb1,tb2,tb3,ta0,ta1,ta2,ta3],dim=0)
        # out_tensor=torch.unsqueeze(out_tensor,0)
        if not out_tensor.dtype == torch.float:
            out_tensor=out_tensor.float()
        return out_tensor

if __name__=="__main__":
    a=Agent()
    b=a.board_to_tensor(np.random.random([BOARD_SIZE,BOARD_SIZE]),np.random.random([BOARD_SIZE,BOARD_SIZE]))
    print(b)