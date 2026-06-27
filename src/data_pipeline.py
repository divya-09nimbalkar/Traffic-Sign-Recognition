import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import cv2
import torchvision.transforms as transforms

class TrafficSignDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.data = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path = self.data.iloc[idx, 0]
        label = self.data.iloc[idx, 1]

        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if self.transform:
            img = self.transform(img)

        # Convert label to integer class index
        label_map = {"Stop":0, "Yield":1, "SpeedLimit":2, "NoEntry":3}
        label_idx = label_map[label]

        return img, label_idx

def get_dataloader(batch_size=32):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((64,64)),
        transforms.Normalize((0.5,), (0.5,))
    ])
    dataset = TrafficSignDataset("data/processed/traffic_signs.csv", transform=transform)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    return loader
