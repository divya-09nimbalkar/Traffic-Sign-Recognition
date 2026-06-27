import torch
from src.model import build_model

def test_model_output_shape():
    net = build_model(num_classes=4)  # Stop, Yield, SpeedLimit, NoEntry
    dummy_input = torch.randn(1, 3, 64, 64)  # batch of 1 image
    output = net(dummy_input)
    assert output.shape == (1, 4)  # 4 classes
