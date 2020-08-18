from chess import *
from board import Board, BOARD_SIZE


class Player:

    def __init__(self, series_num):
        self.chesses = [
            chess0(), chess1(), chess2(), chess3(), chess4(), chess5(), chess6(),
            chess7(), chess8(), chess9(), chess10(), chess11(), chess12(), chess13(),
            chess14(), chess15(), chess16(), chess17(), chess18(), chess19(), chess20()
        ]
        self.used = [
            False for _ in range(len(self.chesses))
        ]
        self.player_series_num = series_num

    def get_policy_set(self, board: Board, first_step=False):
        policy_set = []
        for i in range(len(self.chesses)):
            if self.used[i]:
                policy_set.append(())
            else:
                this_policy = []
                this_chess = self.chesses[i]
                reverses = this_chess.reverse_max
                rotates = this_chess.rotate_max
                for m in range(reverses):
                    for n in range(rotates):
                        this_chess.change_to(reverse_times=m, rotate_times=n)
                        this_shape = this_chess.chess.shape
                        for i in range(BOARD_SIZE - this_shape[0]):
                            for j in range(BOARD_SIZE - this_shape[1]):
                                if board.check_legal((i, j), self.player_series_num, this_chess, first_step=first_step):
                                    this_policy.append((m, n, i, j))
                policy_set.append(tuple(this_policy))
        return policy_set

    def make_a_move(self, board: Board, chess_series, position_and_state=(0, 0, 0, 0), first_step=False):
        self.chesses[chess_series].change_to(position_and_state[2], position_and_state[2])
        if board.check_legal((position_and_state[0], position_and_state[1]), self.player_series_num,
                             self.chesses[chess_series], first_step=first_step):
            self.used[chess_series] = True
            board.add_chess((position_and_state[2], position_and_state[3]), self.player_series_num,
                            self.chesses[chess_series])
            return True
        else:
            self.chesses[chess_series].reset()
            return False

    def reset(self):
        for eachchess in self.chesses:
            eachchess.reset()
        for i in range(len(self.used)):
            self.used[i] = False
