# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from problem_1_25.p003_largest_prime_factor import Eratosthenes_sieve
import numpy as np


def get_product_of_primes(number):
    prime_list = np.array(Eratosthenes_sieve(number))
    return prime_list.prod()


def is_divisible(numerator, denominator):
    return numerator % denominator == 0


def smallest_multiple(number):
    # number has to be at least as large as the product of all primes lower than n
    prime_product = get_product_of_primes(number)
    smallest_number = prime_product
    while True:
        for denominator in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
            if not is_divisible(smallest_number, denominator):
                smallest_number += 1
                _skip = True
                continue
        if _skip:
            _skip = False
            continue
        return smallest_number


if __name__ == '__main__':
    print(smallest_multiple(20))
