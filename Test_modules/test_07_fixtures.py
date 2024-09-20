import pytest

@pytest.fixture
def setupfunc():
    print("fixture function")
    places=['Boudh','Bhubaneswar','Cuttack','Rourkela','Berhampur']
    return places    

def test_myfunc(setupfunc):
    print("This is test function")
    assert setupfunc[::-2]==['Berhampur','Cuttack','Boudh']