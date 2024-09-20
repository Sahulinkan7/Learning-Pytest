import pytest

@pytest.fixture
def fix1():
    print("IN FIXTURE 1")
    yield [1,2,3]
    print("closing fixture 1")

    
    
@pytest.fixture
def fix2():
    print("IN FIXTURE 2")
    yield 2,4,6
    print("closing fixture 2")
    
def test_fix(fix1,fix2):
    print("testing multiple fixtures")
    assert len(fix1)==len(fix2)
    
