from src.maths_operation import op_Add,op_div,op_mul,op_Sub


def test_add_1():
    print("Test case 01 : Test case for addition operation",end=" ")
    assert op_Add(9,19)==28
    
def test_add_2():
    print("Test case 02 : Test case for addition operation",end=" ")
    assert op_Add(10,11)==21
    
def test_mul_1():
    print("Test case 01 : Test case for multiplication operation",end=" ")
    assert op_mul(10,6)==60
    
def test_mul_2():
    print("Test case 02 : Test case for multiplication operation",end=" ")
    assert op_mul("a",6)=="aaaaaa"
    
def test_mul_3():
    print("Test case 03 : Test case for multiplication operation",end=" ")
    assert op_mul("aa",5)=="aaaaaaaaaa"
    
def test_mul_4():
    print("Test case 04 : Test case for multiplication operation",end=" ")
    assert op_mul("aa",4)=="aaaaaaaa"
    
def test_tuple():
    print("Test case 01 : Test case for assert with tuple",end=" ")
    assert 4 in (1,4,5)
    
def test_string():
    print("Test case 01 : Test case for assert with strings",end=" ")
    assert "ab" in "abrgfcd"
    
def test_list():
    print("Test case 01 : Test case for assert with list",end=" ")
    assert [1,2] in [1,4,5,[1,3]]
    
def test_obj():
    print("Test case 01 : Test case for assert with list type object",end=" ")
    l=list()
    assert type(l)==list