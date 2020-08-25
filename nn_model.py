import torch
import torchvision.models as models
import torch.nn as nn

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
        x = torch.flatten(x)  # batch_size*256
        x = self.fc1(x)  # batch_size*1024
        x = self.fc2(x)  # batch_size*1
        return x

nn_model=Identicle_nn().to(device)

criterion=nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(nn_model.parameters())