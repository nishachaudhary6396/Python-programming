import pytest
from ecommerce import calculate_total

def test_valid_total():
    assert calculate_total([100,200],0.1) == 330

def test_negative_price():
    with pytest.raises(ValueError,match="price can not be negative"):
        calculate_total([100,-50],0.1)

def test_invalid_tax():
    with pytest.raises(ValueError,match="Invalid tax rate"):
        calculate_total([100,200],1.5)