import pytest
import numpy as np
from problem_1_25.LargestPalindromeProduct import is_palindrome, generate_product_table


@pytest.mark.parametrize('potential_palindrome', [12321, 1221, 99999, 49122194])
def test_is_palindrome(potential_palindrome):
    assert is_palindrome(potential_palindrome) is True


def test_generate_product_table():
    product_table = generate_product_table(1, 4)
    product_table_fixture = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
    assert (product_table == product_table_fixture).all()


#def test_get_largest_palindrome():
#    []
