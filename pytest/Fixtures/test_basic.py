#fixtures provide setup data before test execution
# avoid code repetion

import pytest
@pytest.fixture
# def stored_data():
#     return 10
# def test_data(stored_data):
#     assert stored_data == 10

def input_list():
    return [1,2,3,4,5]

def test_sum(input_list):
    assert sum(input_list) == 15

def test_length(input_list):
    assert len(input_list) == 5