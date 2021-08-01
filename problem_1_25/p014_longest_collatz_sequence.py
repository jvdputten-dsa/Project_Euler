import numpy as np


def get_collatz_length(number):
    collatz_length = 1
    while True:
        if number == 1:
            return collatz_length

        if number % 2 == 0:
            number = number / 2
        else:
            number = number*3 + 1
        collatz_length += 1

n_to_check = 1000000
collatz_lengths = np.zeros(n_to_check)

for i in range(n_to_check):
    collatz_lengths[i] = get_collatz_length(i+1)
print(np.argmax(collatz_lengths) + 1)
