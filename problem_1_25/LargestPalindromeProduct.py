import numpy as np


def generate_product_table(start, end):
    number_vector = np.arange(start, end, 1)
    product_table = number_vector * number_vector[:, None]
    return product_table


def is_palindrome(number):
    strnumber = str(number)
    if strnumber == strnumber[::-1]:
        return True
    else:
        return False


def get_largest_palindrome(potential_palindromes):
    for potential_palindrome in potential_palindromes:
        if is_palindrome(potential_palindrome):
            return potential_palindrome
    return 'no palindromes found'


def main():
    product_table = generate_product_table(100, 1000)
    potential_palindromes = np.sort(product_table.flatten())[::-1]
    print(get_largest_palindrome(potential_palindromes))


if __name__ == '__main__':
    main()




