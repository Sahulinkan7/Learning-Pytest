from src.maths_operation import op_Add,op_div,op_mul,op_Sub


class Testoperations:
    def test_add_01(self):
        assert op_Add(9,7)==16
        
    def test_add_02(self):
        assert op_Add(89,0.5)==89.5
        
        
        
def test_div_01():
    assert op_div(10,2)==5