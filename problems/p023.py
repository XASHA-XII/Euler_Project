import itertools

from p006 import sum_formula
from p021 import sum_of_divisors

'''
https://projecteuler.net/problem=23
Non-abundant sums
'''


def main() -> int:
    '''Returns the sum of all numbers that cannot be written as the sum of two abundants. 
    A upper limit of this set is given by 28123. We sum all sums of two abundants and subtract it from the small Euler
    of the limit of the set.'''
    LIMIT = 28123

    abundants = (z for z in range(1, LIMIT+1) if is_abundant(z))
    sum_of_abundants = set(sum(x) for x in itertools.combinations_with_replacement(
        abundants, 2) if sum(x) <= LIMIT)

    largest_no_sum = max(sum_of_abundants)
    result = sum_formula(largest_no_sum) - sum(sum_of_abundants)
    return result


def is_abundant(n: int) -> bool:
    '''
    Checks whether a positive integer n is abundant, i.e. if the sum of its divisors exceeds n.
    Example: 1+2+3+4+6=16 > 12
    '''
    result = (sum_of_divisors(n) > n)
    return result


if __name__ == '__main__':
    result = main()
    print(result)
