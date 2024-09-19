import pytest
from src.maths_operation import op_mul

@pytest.mark.parametrize("a",[5,6])
def test_param01(a):
    assert a>4
    
@pytest.mark.sanity
@pytest.mark.parametrize("input,output",[(5,4),(9,8)])
def test_param02(input,output):
    assert input-1==output
    
    
@pytest.mark.sanity
@pytest.mark.parametrize("a,b,output",[(5,4,20),(9,8,72)])
def test_param03(a,b,output):
    assert op_mul(a,b)==output