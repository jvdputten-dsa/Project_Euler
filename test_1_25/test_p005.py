import pytest
from problem_1_25.p005_smallest_multiple import is_divisible, smallest_multiple


@pytest.mark.parametrize('numerator, denominator, expected', [(20, 4, True), (27, 9, True), (12, 8, False)])
def test_is_divisible(numerator, denominator, expected):
    assert expected is is_divisible(numerator, denominator)


def test_smallest_multiple():
    assert smallest_multiple(10) == 2520


