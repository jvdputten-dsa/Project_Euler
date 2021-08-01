import numpy as np
from p003_largest_prime_factor import Eratosthenes_sieve
# What is the value of the first triangle number to have over five hundred divisors?


def count_exponents(number):
    exponents = np.zeros_like(prime_list)
    for i, prime in enumerate(prime_list):
        if number == 1:
            return exponents
        while number % prime == 0:
            number = number/prime
            exponents[i] += 1


def get_n_triangle_numbers(n, start=0):
    return np.cumsum(np.arange(start+1, start+1+n))


def get_n_prime_factors(exponents):
    exponents = exponents[np.where(exponents > 0)]
    exponents += 1
    return exponents.prod() + 1


if __name__ == '__main__':
    prime_list = Eratosthenes_sieve(100000)
    triangle_numbers = get_n_triangle_numbers(100000)
    for triangle_number in triangle_numbers:
        exponents = count_exponents(triangle_number)
        n_prime_factors = get_n_prime_factors(exponents)
        if n_prime_factors > 500:
            print(triangle_number)
            break
