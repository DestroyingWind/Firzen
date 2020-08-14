from chess import *


class player():

    def __init__(self):
        self.chesses = [
            chess0(), chess1(), chess2(), chess3(), chess4(), chess5(), chess6(),
            chess7(), chess8(), chess9(), chess10(), chess11(), chess12(), chess13(),
            chess14(), chess15(), chess16(), chess17(), chess18(), chess19(), chess20()
        ]
        self.used = [
            False for _ in range(len(self.chesses))
        ]

    def get_action_set(self, board):
        for i in range(len(self.chesses)):
            if self.used[i]:
                continue
            else:
                this_chess = self.chesses[i]

