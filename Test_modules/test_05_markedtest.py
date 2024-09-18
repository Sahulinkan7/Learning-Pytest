import pytest 

@pytest.mark.sanity
def test_str1():
    s="linkankumarsahu"
    assert s.capitalize()=="Linkankumarsahu"
    
    

@pytest.mark.sanity
@pytest.mark.split
def test_str2():
    email="sahulinkan7@gmail.com"
    assert email.split("@")[0]=="sahulinkan7"