from Array import Array


def test_print():
    "Tests if the arrays prints out strings nicely."
    A = Array((4,), 1, 2, 3, 4)
    test_str = f"{A}"
    assert test_str == "[1, 2, 3, 4]"

def test_element_add():
    "Tests element-wise addition with two arrays."
    A = Array((4,), 1, 2, 3, 4)
    B = Array((4,), 4, 3, 2, 1)
    correct = Array((4,), 5, 5, 5, 5)
    assert A+B == correct

def test_scalar_add():
    "Tests addition of an array and a scalar."
    A = Array((4,), 1, 2, 3, 4)
    B = 10
    correct = Array((4,), 11, 12, 13, 14)
    test_add = A+B
    assert test_add==correct

def test_scalar_radd():
    "Tests addition of an array and a scalar works both ways."
    A = Array((4,), 1, 2, 3, 4)
    B = 10
    correct = Array((4,), 11, 12, 13, 14)
    test_add = B+A
    assert test_add == correct

def test_element_sub():
    "Tests element-wise subtraction with two arrays."
    A = Array((4,), 5, 5, 5, 5)
    B = Array((4,), 3, 3, 3, 3)
    correct = Array((4,), 2, 2, 2, 2)
    assert A-B == correct

def test_scalar_sub():
    "Tests subtraction of an array with a scalar."
    A = Array((4,), 11, 12, 13, 14)
    B = 10
    correct = Array((4,), 1, 2, 3, 4)
    test_sub = A-B
    assert test_sub == correct

def test_scalar_rsub():
    "Tests subtraction of a scalar with an array."
    A = Array((4,), 11, 12, 13, 14)
    B = 10
    correct = Array((4,), -1, -2, -3, -4)
    test_sub = B-A
    assert test_sub == correct

def test_element_mul():
    "Tests element-wise multiplication with two arrays."
    A = Array((4,), 1, 2, 3, 4)
    B = Array((4,), 5, 6, 7, 8)
    correct = Array((4,), 5, 12, 21, 32)
    assert A*B == correct

def test_scalar_mul():
    "Tests multiplication of an array with a scalar."
    A = Array((4,), 3, -1, 8, 4)
    B = 10
    correct = Array((4,), 30, -10, 80, 40)
    test_mul = A*B
    assert test_mul == correct

def test_scalar_rmul():
    "Tests multiplication of a scalar with an array."
    A = Array((4,), 3, -1, 8, 4)
    B = 10
    correct = Array((4,), 30, -10, 80, 40)
    test_mul = B*A
    assert test_mul == correct

def test_eq_true():
    "Tests if two identical arrays return True with =="
    A = Array((4,), 1, 2, 3, 4)
    B = Array((4,), 1, 2, 3, 4)
    correct = True
    test_eq = A==B
    assert test_eq == correct

def test_eq_false_shape():
    "Tests if two arrays of different shape return False with =="
    A = Array((4,), 1, 2, 3, 4)
    B = Array((3,), 1, 2, 3)
    correct = False
    test_eq = A==B
    assert test_eq == correct

def test_eq_false_type():
    "Tests if two arrays with different types return False with =="
    A = Array((4,), 1, 2, 3, 4)
    B = Array((4,), 1.0, 2.0, 3.0, 4.0)
    correct = False
    test_eq = A==B
    assert test_eq == correct

def test_eq_false_elements():
    "Tests if two arrays with different elements return False with =="
    A = Array((4,), 1, 2, 3, 4)
    B = Array((4,), 4, 3, 2, 1)
    correct = False
    test_eq = A==B
    assert test_eq == correct

def test_is_equal():
    "Tests if is_equal returns an array of booleans."
    A = Array((5,), 1, 2, 3, 4, 5)
    B = Array((5,), 5, 4, 3, 2, 1)
    correct = Array((5,), False, False, True, False, False)
    test_equal = A.is_equal(B)
    assert test_equal == correct

def test_min_element():
    "Tests if min_element returns the smallest element."
    A = Array((4,), 14, 100, 8, 2.4)
    small = A.min_element()
    assert small == 2.4

def test_add_2D_array():
    "Tests if add works with 2D-arrays"
    A = Array((2,3), 1, 2, 3, 3, 2, 1)
    B = Array((2,3), 3, 2, 1, 1, 2, 3)
    correct = Array((2,3), 4, 4, 4, 4, 4, 4)
    test_add = A+B
    assert test_add == correct
    
def test_sub_2D_array():
    "Tests if sub works with 2D-arrays"
    A = Array((2,3), 3.0, 2, 1, 1, 4.2, 3)
    B = Array((2,3), 1, 2, 1.0, 1.0, 2, 1)
    correct = Array((2,3), 2.0, 0, 0, 0, 2.2, 2)
    test_sub = A-B
    assert test_sub == correct

def test_mul_2D_array():
    "Tests if mul works with 2D-arrays"
    A = Array((2,3), 1, 10, 3, -2, 5, 2)
    B = Array((2,3), 1, 2, 3, 4, 5, 6)
    correct = Array((2,3), 1, 20, 9, -8, 25, 12)
    test_sub = A*B
    assert test_sub == correct

def test_eq_true_2D_array():
    "Tests if two identical 2D-arrays return True with =="
    A = Array((3,2), 1, 2, 3, 4, 5, 6)
    B = Array((3,2), 1, 2, 3, 4, 5, 6)
    correct = True
    test_eq = A==B
    assert test_eq == correct

def test_is_equal_for_2D():
    "Tests if is_equal returns an 2D-array of booleans."
    A = Array((4,2), 1, 2, 3, 4, 5, 6, 7, 8)
    B = Array((4,2), 1, 3, 2, 4, 3, 6, 5, 8)
    correct = Array((4,2), True, False, False, True, False, True, False, True)
    test_equal = A.is_equal(B)
    assert test_equal == correct