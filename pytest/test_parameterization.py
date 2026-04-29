#parametrization allows you to run the same test function multiple times  using @pytest.mark.parametrize

import pytest
@pytest.mark.parametrize("num1,num2,expected",[
    (4,6,10),
    (2,3,5),
    (7,7,14),
    (0,0,0)   # multiple sets of data
])

def test_addition(num1,num2,expected):   #test-function
    assert num1+num2 ==expected

