import pytest
from sanitize import sanitize_input, InputSanitizationError

def test_name_input():
    assert sanitize_input("John Doe!") == "John Doe"


def test_empty_input():
    with pytest.raises(InputSanitizationError, match="emptyyy text"):
        sanitize_input("!@#$%")

def test_payment_input():
    assert sanitize_input("Payment: 100$") == "Payment 100"