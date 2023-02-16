import itertools

from utils import is_prime

'''
https://projecteuler.net/problem=58
Spiral primes
'''


def main() -> int:
    """Returns the first occurance, where the number of primes of corners of a grid of integers
    with sidelength k falls below the threshold .1. A grid is of the form
    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

    Returns:
        int: The grid side length k
    """
    THRESHOLD = .1

    diag_elems = 1
    primes = 0
    for k in itertools.count(3, 2):
        diag_elems += 4
        primes += sum(1 for l in range(1, 4) if is_prime(k**2 - l*(k-1)))
        if primes / diag_elems < THRESHOLD:
            return k


if __name__ == '__main__':
    result = main()
    print(result)
