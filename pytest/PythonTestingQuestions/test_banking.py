import pytest
from banking import transfer, TransferError

def test_successful_transfer():
    assert transfer("1234567890", "9876543210", 500, 1000) == 500

def test_no_amount():
    with pytest.raises(TransferError, match="Invalid amount"):
        transfer("1234567890", "9876543210", 0, 1000)

def test_insufficient_balance():
    with pytest.raises(TransferError, match="Insufficient balance"):
        transfer("1234567890", "9876543210", 1500, 1000)

def test_invalid_account():
    with pytest.raises(TransferError, match="Invalid from account"):
        transfer("12345", "9876543210", 500, 1000)