def operator_Add(in1, in2):
    return in1+in2

def operator_Sub(in1, in2):
    return in1-in2

def operator_Mul(in1, in2):
    return in1*in2

def operator_And(in1, in2):
    return in1&in2

def operator_Or(in1, in2):
    return in1|in2

def operator_Xor(in1, in2):
    return in1^in2

def operator_Xnor(in1, in2):
    return ~(in1^in2)

def test_operator_Add():
    assert operator_Add(1,2) == 3
    print('test_operator_Add---PASS')

def test_operator_Sub():
    assert operator_Sub(2,1) == 1
    print('test_operator_Sub---PASS')

def test_operator_Mul():
    assert operator_Mul(1,2) == 2
    print('test_operator_Mul---PASS')

def test_operator_And():
    assert operator_And(1,2) == (1&2)
    print('test_operator_And---PASS')

def test_operator_Or():
    assert operator_Or(1,2) == (1|2)
    print('test_operator_Or----PASS')

def test_operator_Xor():
    assert operator_Xor(1,2) == (1^2)
    print('test_operator_Xor---PASS')

def test_operator_Xnor():
    assert operator_Xnor(1,2) == ~(1^2)
    print('test_operator_Xnor--PASS')











