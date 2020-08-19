import numpy as np
import random
import time
from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        for i in range(4):
            self.players.append(Player(0))
        self.active=[True for _ in range(4)]

    def one_game(self,human_player=(True,True,True,True)):
        run_flag=True
        first_flag=True
        while run_flag:
            for i in range(4):
                if not self.active[i]:
                    continue
                if human_player[i]:
                    print("it's now the turn owned by player {}, it's a human player.".format(i+1))
                    self.human_move(i,first_flag)
                else:
                    print("it's now the turn owned by player {}, it's a computer player.".format(i + 1))
                    self.auto_move(i,first_flag)
                self.board.rotate()
            self.board.print()
            if sum(self.active)==0:
                run_flag=False
            if first_flag:
                first_flag=False
        result=self.board.count()
        for i in range(result.__len__()):
            print("player %d gets %d scores." % (i+1,result[i]))
        print("player %d has won this game." % (np.argmax(np.array(result))+1))
        return True

    def auto_move(self,player_series,first_flag=False):
        # todo training module and follow policy module.
        this_player=self.players[player_series]
        policy_set=this_player.get_policy_set(self.board,first_flag)
        policies=[]
        for i in range(policy_set.__len__()):
            for j in range(policy_set[i].__len__()):
                policies.append((i,policy_set[i][j][0],policy_set[i][j][1],policy_set[i][j][2],policy_set[i][j][3]))
        if policies.__len__()==0:
            self.active[player_series]=False
            return False
        policy=random.choice(policies)
        print(policy)
        this_player.make_a_move(self.board,policy[0],policy[1:],first_flag)
        print("player {} has automatically moved.".format(player_series+1))
        return True

    def human_move(self,player_series,first_flag=False):
        this_player=self.players[player_series]
        selected=-1
        while True:
            instruct=input("please input your instruction:")
            if instruct=="showchesses":
                for i in range(this_player.chesses.__len__()):
                    if not this_player.used[i]:
                        print("chess " ,i , " is unused:")
                        this_player.chesses[i].print()
            elif instruct[:6]=="select":
                try:
                    selected=int(instruct.strip().split(" ")[-1])
                    if this_player.used[selected]:
                        print("sorry!\nthis chess is used,please select another one.")
                        selected=-1
                    else:
                        this_player.chesses[selected].print()
                        print("chess %d is successfully selected!" % (selected))
                except Exception as e:
                    print(e)
            elif instruct[:6] == "rotate":
                if selected=="-1":
                    print("please select a chess first.")
                    continue
                instruct=instruct.strip().split(" ")
                if instruct.__len__()==1:
                    this_player.chesses[selected].rotate()
                    print("the chess has been rotated to:")
                    this_player.chesses[selected].print()
                else:
                    try:
                        rotate_times=int(instruct[1])
                        for i in range(rotate_times):
                            this_player.chesses[selected].rotate()
                        print("the chess has been rotated %d times to:" % (rotate_times))
                        this_player.chesses[selected].print()
                    except:
                        print("input error, please follow the format 'rotate %d' where %d is the rotating times.")
            elif instruct[:7] == "reverse":
                if selected == "-1":
                    print("please select a chess first.")
                    continue
                this_player.chesses[selected].reverse()
                print("the chess has been reversed to:")
                this_player.chesses[selected].print()
            elif instruct == "hint":
                hint=this_player.get_policy_set(self.board,first_flag)
                print("reverse\trotate\tx\ty")
                for i,eachchess in enumerate(hint):
                    print("chess %d" % (i))
                    for eachtuple in eachchess:
                        print("%d\t%d\t%d\t%d" % eachtuple)
            elif instruct[:9]=="makemove":
                if selected == -1:
                    print("please select a chess first.")
                    continue
                instruct=instruct.strip().split(" ")
                try:
                    x=int(instruct[1])
                    y=int(instruct[2])
                except Exception as e:
                    print(e)
                    print("failed to make this move due to illegal input")
                    continue
                position_tuple=(x,y,this_player.chesses[selected].reverse_flag,this_player.chesses[selected].rotate_flag)
                if this_player.make_a_move(self.board,selected,position_tuple):
                    print("successfully made a move!")
                    break
                else:
                    print("failed to make a move due to the position or shape illegal!")
            elif instruct[:9]=="quickmove":
                instruct=instruct.strip().split(" ")
                if not instruct.__len__()==6:
                    print("input insufficient or too much, please check it.")
                else:
                    instruct=[instruct[i] if i == 0 else int(instruct[i]) for i in range(instruct.__len__()) ]
                    if this_player.make_a_move(self.board,instruct[1],tuple(instruct[2:]),first_flag):
                        print("successfully made a move!")
                        break
                    else:
                        print("failed to make a move due to the position or shape illegal, or maybe this chess is already used!")
            elif instruct=="showboard":
                self.board.print()
            elif instruct=="giveup":
                self.active[player_series]=False
                print("you have given up this match.")
                break
            else:
                print("illegal input!!\nplease choose one instruction according to the documents.")
        return False