import game
from agent import Agent

if __name__=="__main__":
    newgame=game.Game()
    # newgame.one_game(human_player=(False,False,False,False))
    agent=Agent(epsilon=1)
    x=newgame.gen_training_data(1,agent)
    for a in x:
        print(a)