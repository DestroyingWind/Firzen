import torch
import torch.nn as nn
from torch.utils.data import Dataset
import numpy as np
from board import BOARD_SIZE


device=torch.device("cuda" if torch.cuda.is_available() else "cpu")

class Identicle_nn(nn.Module):
    def __init__(self):
        super(Identicle_nn, self).__init__()
        self.conv1 = nn.Conv2d(8, 64, 5, 1)
        self.conv2 = nn.Conv2d(64, 128, 3, 1)
        self.conv3 = nn.Conv2d(128, 256, 3, 1)
        self.fc1 = nn.Linear(256, 1024)
        self.fc2 = nn.Linear(1024, 1)

    def forward(self, x):
        # batch_size*7*20*20
        x = self.conv1(x)  # batch_size*64*16*16
        x = nn.functional.max_pool2d(x, 2)  # batch_size*64*8*8
        x = nn.functional.relu(x)  # batch_size*64*8*8
        x = self.conv2(x)  # batch_size*128*6*6
        x = nn.functional.max_pool2d(x, 2)  # batch_size*128*3*3
        x = nn.functional.relu(x)  # batch_size*128*3*3
        x = self.conv3(x)  # batch_size*256*1*1
        x = torch.flatten(x,1,-1)  # batch_size*256
        x = self.fc1(x)  # batch_size*1024
        x = self.fc2(x)  # batch_size*1
        return x


class Trainer:
    def __init__(self,model:nn.Module,learning_rate:float,dataset:Dataset,loss=nn.CrossEntropyLoss(),decay=True):
        self.model=model
        self.lr=learning_rate
        self.loss=loss
        self.optimizer=torch.optim.Adam(self.model.parameters(),self.lr)
        self.dataset=dataset
        self.dataloader=torch.utils.data.DataLoader(self.dataset,batch_size=4,shuffle=True)
        self.data_iter=iter(self.dataloader)
        self.data_len=self.dataloader.__len__()

    def train(self):
        for i in range(self.data_len):
            x,y=self.data_iter.__next__()
            y=y.unsqueeze(1)
            y_pred=self.model(x)
            loss=self.loss(y,y_pred)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

class My_dataset(Dataset):
    def __init__(self,x0,x1,y):
        super(My_dataset,self).__init__()
        self.x0=np.load(x0,allow_pickle=True)
        self.x1=np.load(x1,allow_pickle=True)
        self.y=np.load(y,allow_pickle=True)

    def __len__(self):
        return self.x0.__len__()

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
        tensor_before = torch.tensor(before, dtype=torch.float,device=device)
        tensor_after = torch.tensor(after, dtype=torch.float,device=device)
        t0=torch.tensor(np.zeros([BOARD_SIZE,BOARD_SIZE]),dtype=torch.float,device=device)
        t1=torch.tensor(np.ones([BOARD_SIZE,BOARD_SIZE]),dtype=torch.float,device=device)
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

    def __getitem__(self, item):
        x0=self.x0[item]
        x1=self.x1[item]
        y=self.y[item]
        return self.board_to_tensor(x0,x1),torch.tensor(y,dtype=torch.float,device=device)