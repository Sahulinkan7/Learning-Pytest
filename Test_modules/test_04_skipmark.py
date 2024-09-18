import pytest

@pytest.mark.skip(reason="just skipped with no reason")
def test_str():
    s="abcdefghijklmnopqrstuvwxyz"
    assert s[-1]=="z"==s[25]
    
def test_str2():
    s="abcdefghijklmnopqrstuvwxyz"
    assert s[:]=="abcdefghijklmnopqrstuvwxyz"
    
@pytest.mark.skipif(1 in (1,2,3),reason="testing and skiping")
def test_str3():
    s="abcdefghijklmnopqrstuvwxyz"
    assert s[:]=="abcdefghijklmnopqrstuvwxyz"