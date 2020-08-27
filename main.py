import game
from nn_model import *
import os
import numpy as np
import torch
from agent import Agent

stages=100
epoches=100
old_version=None

if __name__=="__main__":
    newgame=game.Game()
    # newgame.one_game(human_player=(False,False,False,False))
    model=Identicle_nn().to(device)
    version=[]
    for eachfile in os.listdir("checkpoints"):
        if eachfile[:5]=="model" and eachfile[-4:]==".pkl":
            version.append(int(eachfile[5:-4]))
    if not old_version:
        if not version.__len__()==0:
            model.load_state_dict(state_dict=torch.load("model"+str(max(version))+".pkl"))
    else:
        if old_version in version:
            model.load_state_dict(state_dict=torch.load("model" + str(max(old_version)) + ".pkl"))
    agent = Agent(epsilon=1,model=model)
    for stage in range(stages):
        print("stages:",(stage+1))
        agent.epsilon=(1/(stage+1))
        print("epsilon is set to %.3f" % (agent.epsilon))
        datas=newgame.gen_training_data(epoches,agent)
        for i,a in enumerate(datas):
            b=np.stack(a)
            np.save(file=os.path.join("data",str(i)+".npy"),arr=b,allow_pickle=True)
        trainer = Trainer(model=model, learning_rate=0.3*100/(100+stage),dataset=My_dataset("data/0.npy","data/1.npy","data/2.npy"),loss=torch.nn.MSELoss())
        trainer.train()
        if (stage+1)%50 == 0:
            print("saving weights at %d stages." % (stage+1))
            torch.save(model.state_dict(),"checkpoints/model%d.pkl" % (stage+1))