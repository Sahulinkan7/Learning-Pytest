import pytest

@pytest.fixture
def setupfunc():
    print("fixture function")
    

def test_myfunc(setupfunc):
    print("This is test function")
    assert 1==1