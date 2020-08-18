from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        for i in range(4):
            self.players.append(Player(i))
        self.active=[True for _ in range(4)]

    def main_loop(self,human_player=(True,True,True,True)):
        run_flag=True
        first_flag=True
        while run_flag:
            for i in range(4):
                if not self.active[i]:
                    continue
                if human_player[i]:
                    self.human_move()
                else:
                    self.auto_move(first_flag)
            if sum(self.active)==0:
                run_flag=False
            if first_flag:
                first_flag=False
        return True

    def auto_move(self,first_flag=False):
        # todo automatically move according to the learned policy
        pass

    def human_move(self):
        # todo human interact interface to move one step
        pass