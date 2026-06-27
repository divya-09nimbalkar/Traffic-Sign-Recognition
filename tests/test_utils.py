import pytest
from src import utils

def test_utils_placeholder():
    # Example: if you add a helper function in utils.py
    if hasattr(utils, "normalize_path"):
        path = utils.normalize_path("data/raw/stop_0.png")
        assert isinstance(path, str)
    else:
        pytest.skip("No utils functions implemented yet")
