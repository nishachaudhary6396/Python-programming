#Pytest is a popular testing framework in python used to write and run tests for your code...it helps you check whether your code is working correctly or not.

def func(x):
    return x+1
def test_answer():
    assert func(3) ==4
def test_add():
    assert func(1) ==2
def test_add2():
    assert func(2) ==3


# def test_values():
#     assert 5 > 3        
#     assert "hello" == "hello"    #both will pass

def multiply(a,b):
    return a * b
def test_multiply():
    assert multiply(2,3) == 6

    