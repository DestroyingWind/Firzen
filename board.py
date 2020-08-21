from chess import *

BOARD_SIZE = 20


class Board:
    color={-1:"w",0:"r",1:"y",2:"b",3:"g"}
    def __init__(self):
        self.base_board = np.ones([BOARD_SIZE, BOARD_SIZE],dtype=np.int8) * (-1)
        self.rotate_flag = 0

    def add_chess(self, position=(0, 0), player_series=0, this_chess=chess()):
        shape = this_chess.chess.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                if this_chess.chess[i, j]:
                    self.base_board[position[0] + i, position[1] + j] = player_series

    def remove_chess(self, position=(0, 0),  this_chess=chess()):
        shape = this_chess.chess.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                if this_chess.chess[i, j]:
                    self.base_board[position[0] + i, position[1] + j] = -1

    def rotate(self):
        self.base_board = np.rot90(self.base_board, -1)
        self.rotate_flag += 1
        self.rotate_flag %= 4
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.base_board[i,j]==-1:
                    continue
                else:
                    self.base_board[i,j]-=1
                    self.base_board[i,j]%=4

    def check_legal(self, position=(0, 0), player_series_num=0, this_chess=chess(), first_step=False):
        if first_step:
            if this_chess.chess[0, 0] and position[0]==0 and position[1]==0:
                return True
            else:
                return False
        shape = this_chess.chess.shape
        must_flag = False
        for i in range(shape[0]):
            for j in range(shape[1]):
                if not this_chess.chess[i, j]:
                    continue
                forbid_any = [
                    (position[0] + i, position[1] + j),
                    (position[0] + i + 1, position[1] + j),
                    (position[0] + i - 1, position[1] + j),
                    (position[0] + i, position[1] + j + 1),
                    (position[0] + i, position[1] + j - 1)
                ]
                must_one = [
                    (position[0] + i + 1, position[1] + j + 1),
                    (position[0] + i + 1, position[1] + j - 1),
                    (position[0] + i - 1, position[1] + j + 1),
                    (position[0] + i - 1, position[1] + j - 1)
                ]
                if not self.base_board[forbid_any[0][0], forbid_any[0][1]] == -1:
                    return False
                for eachposition in forbid_any:
                    if self.base_board[eachposition[0], eachposition[1]] == player_series_num:
                        return False
                for eachposition in must_one:
                    if self.base_board[eachposition[0], eachposition[1]] == player_series_num:
                        must_flag = True
        if must_flag:
            return True
        else:
            return False

    def count(self):
        result=[0,0,0,0]
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.base_board[i,j]==-1:
                    continue
                else:
                    result[self.base_board[i,j]]+=1
        return result

    def plot_board(self):
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        loc = plticker.MultipleLocator(base=1)
        ax.xaxis.set_major_locator(loc)
        ax.yaxis.set_major_locator(loc)
        ax.set_xlim(0,BOARD_SIZE)
        ax.set_ylim(0,BOARD_SIZE)
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                place = np.array([i, j])
                color=self.color[self.base_board[i,j]]
                rec = patches.Rectangle(xy=place, width=1, height=1, color=color)
                ax.add_patch(rec)
        plt.grid(which="major")
        plt.show()

    def print(self):
        shape=self.base_board.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                print(self.base_board[i,j]+1,end="")
            print("\n",end="")

    def reset(self):
        self.__init__()

if __name__=="__main__":
    board=Board()
    board.print()