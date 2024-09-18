from src.raise_exceptions import raise_exp,raise_valerr
from src.maths_operation import op_div
import pytest

def test_exc():
    with pytest.raises(ZeroDivisionError):
        raise_exp()
        
def test_valerr():
    with pytest.raises(ZeroDivisionError):
        raise_valerr()
        
def test_valerr2():
    with pytest.raises(ValueError):
        raise_valerr()
        
def test_div():
    with pytest.raises(ZeroDivisionError):
        op_div(45,0)