import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

class Classifier(nn.Module):

    def __init__(self):
        super().__init__()
        self.resnet = torchvision.models.resnet18()
        self.resnet.fc = nn.Linear(512, 2)
        
    
    def forward(self, x):
        return self.resnet(x)

image_transform = transforms.Compose([
    transforms.Resize(96),
    transforms.CenterCrop(96),
    transforms.ToTensor()
])