import pytest
def test_value_error():
    with pytest.raises(ValueError):
        int("abc")