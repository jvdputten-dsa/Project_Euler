import pytest
from problem_1_25.LargestPalindromeProduct import is_palindrome


@pytest.mark.parametrize('potential_palindrome', [12321, 1221, 99999, 49122194])
def test_is_palindrome(potential_palindrome):
    assert is_palindrome(potential_palindrome) is True
