import pytest
from src.data_pipeline import get_dataloader

def test_dataloader_returns_batches():
    loader = get_dataloader(batch_size=2)
    batch = next(iter(loader))
    imgs, labels = batch
    assert imgs.shape[0] == 2  # batch size
    assert len(labels) == 2
