import torch.nn as nn
import torchvision.models as models

def build_model(num_classes=43):
    """
    Builds a ResNet18 model for traffic sign classification.
    """
    net = models.resnet18(weights=None)  # no pretrained weights
    net.fc = nn.Linear(net.fc.in_features, num_classes)
    return net
