import torch
import torchvision.models as models
import torch.nn as nn

resnet18=models.resnet18()

class identicle__nn(nn.Module):
    def __init__(self):
        super(identicle__nn,self).__init__()
        self.conv1=nn.Conv2d(7,64,5,1)#16
        self.conv2=nn.Conv2d(64,128,3,1)#6
        self.conv3=nn.Conv2d(128,256,3,1)
        self.fc1=nn.Linear(256,1024)
        self.fc2=nn.Linear(1024,1)

    def forward(self,x):
        x=self.conv1(x)
        x=nn.functional.max_pool2d(x,2)
        x=nn.functional.relu(x)
        x=self.conv2(x)
        x=nn.functional.max_pool2d(x,2)
        x=nn.functional.relu(x)
        x=self.conv3(x)
        x=torch.flatten(x)
        x=self.fc1(x)
        x=self.fc2(x)
        return x