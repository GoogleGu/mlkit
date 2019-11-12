import sys

sys.path.append('.')

import matplotlib.pyplot as plt
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision import transforms

from utils import show_databatch

data_dir = '/Users/arthur/Code/Dataset/vehicles/'

data_transform = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
    ])

folder = ImageFolder(root=data_dir, transform=data_transform)

loader = DataLoader(
        folder, batch_size=8,
        shuffle=True, num_workers=1
    )

inputs, classes = next(iter(loader))
show_databatch(inputs, classes)