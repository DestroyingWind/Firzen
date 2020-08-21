import nn_model
import torch


nm=nn_model.identicle__nn()

random_data=torch.rand(1,7,20,20,)
result=nm(random_data)
print(result)