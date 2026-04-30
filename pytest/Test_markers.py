# markers in pytest are special decorators use to control the behavior of test cases,  ....they tell pytest how to handle specific tests lieke whether to skip them, expect them to fail, group them.  ....they are built-in markers and Custom Markers

# @pytest.mark.skip
import pytest
import sys    # we use sys to know the version or system details
@pytest.mark.skip
def test_skip_example():
    assert 1==2

# @pytest.mark.skipif
@pytest.mark.skipif(sys.version_info <(3,10), reason ="Requires Python 3.10+")   #reason will show when the test is skipped
def test_version():
    assert True

# @pytest.mark.xfail
@pytest.mark.xfail
def test_fail():
    assert 2 == 3   #pytest does not treat it as error


#custom markers -> it is user defined labels

# @pytest.mark.slow
# def test_slow():
#     assert True

# @pytest.mark.fast
# def test_fast():
#     assert True

# def login(user,password):
#     if user == "admin" and password == "1234":
#         return "Success"
#     return "fail"
# @pytest.mark.regression
# def test_login():
#     assert login("admin","1234") =="Success"




