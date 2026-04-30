import pytest
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        10/0