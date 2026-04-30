import pytest
def login(user):
    if user != "admin":
        raise ValueError("Invalid user")

def test_login_error():
    with pytest.raises(ValueError):
        login("user")