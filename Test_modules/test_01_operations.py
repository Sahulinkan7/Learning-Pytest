from src.maths_operation import op_Add,op_div,op_mul,op_Sub


def test_add_1():
    print("this is the first test case for addition operation")
    assert op_Add(9,19)==28
    
def test_add_2():
    assert op_Add(10,11)==21
    
def test_mul_1():
    assert op_mul(10,6)==60
    
def test_mul_2():
    assert op_mul("a",6)=="aaaaaa"
    
def test_mul_3():
    assert op_mul("aa",5)=="aaaaaaaaaa"
    
def test_mul_3():
    assert op_mul("aa",4)=="aaaaaaaa"