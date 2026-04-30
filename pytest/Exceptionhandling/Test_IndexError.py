import pytest
def test_index_error():
    list = [1,2,3]
    with pytest.raises(IndexError):
        list[10]