# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from problem_1_25.p003_largest_prime_factor import Eratosthenes_sieve

# use sieve from problem 3 to get enough prime numbers
primes = Eratosthenes_sieve(150000)

prime = primes[10000]
print(prime)