import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from calculator import add, multiply, subtract, divide

# Python

def test_add_positive_numbers():
    assert add(2, 3) == 5




def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6




def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2





def test_divide_positive_numbers():
    assert divide(6, 3) == 2


