import numpy as np

number_vector = np.arange(1, 1000, 1)

def is_palindrome(number):
    strnumber= str(number)
    if strnumber == strnumber[::-1]:
        return True
    else:
        return False

def get_largest_palindrome(potential_palindromes):
    for potential_palindrome in potential_palindromes:
        if is_palindrome(potential_palindrome):
            return potential_palindrome
    return 'no palindromes found'


potential_palindromes = list(set(number_vector*number_vector[:,None].flatten()))
potential_palindromes = np.sort(potential_palindromes)[::-1]

print(get_largest_palindrome(potential_palindromes))




