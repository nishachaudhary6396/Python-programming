import pytest
from employee import validate_employee

def test_valid_employee():
    assert validate_employee("EMP-1234","nisha@company.com") == "Valid Employee"

def test_invalid_id():  # invalid emp id
    with pytest.raises(ValueError,match="Invalid Employee Id"):
        validate_employee("EMP-12","nisha@gmail.com")

def test_invalid_email():
    with pytest.raises(ValueError,match="Invalid email"):
        validate_employee("EMP-1234","nisha@gmail.com")

