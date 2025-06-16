import pytest
from calculator import add, multiply, subtract, divide

# Python

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_by_zero():
    assert multiply(0, 10) == 0

def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_result():
    assert subtract(3, 5) == -2

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_divide_positive_numbers():
    assert divide(6, 3) == 2

def test_divide_negative_numbers():
    assert divide(-6, 3) == -2

def test_divide_by_one():
    assert divide(7, 1) == 7

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)