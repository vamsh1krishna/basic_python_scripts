import pytest

@pytest.mark.run_these_please
def test_failing():
    assert (3,2,1) == (1,2,3)