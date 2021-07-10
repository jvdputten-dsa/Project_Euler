import numpy as np
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def Eratosthenes_sieve(number):
    primes_list = [2]
    is_prime_list = np.array([True]*number)

    while True:
        c_prime = primes_list[-1]
        is_prime_list[c_prime*2-1::c_prime] = False # multiples of prime are not prime
        try:
            primes_list.append(np.where(is_prime_list[c_prime:] == True)[0][0]+1+c_prime)
        except IndexError:
            return primes_list


def calc_prime_factors(number, prime_list):
    factor_list = []
    for prime in prime_list:
        if number % prime == 0:
            number/= prime
            factor_list.append(prime)
    return factor_list


# get some primes
prime_list = Eratosthenes_sieve(10000)

print(calc_prime_factors(600851475143, prime_list))





