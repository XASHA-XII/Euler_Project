import itertools

from utils import p_adic_expansion
'''
https://projecteuler.net/problem=30
Digit fifth powers
'''


def main() -> int:
    """Returns the sum of all numbers that can be written as its digit sum to the power 5. Example for 4:
        1634 = 1**4 + 6**4 + 3**4 + 4**4

    Returns:
        int: sum
    """
    POWER = 5
    LIMIT = get_limit()
    result = 0
    for n in range(2, LIMIT):
        if is_sum_of_powers(n, POWER):
            result = result + n
    return result


def is_sum_of_powers(n: int, power: int) -> bool:
    """Checks if a integer number can be written as its digit sum to the power 5

    Args:
        n (int): integer
        power (int): power

    Returns:
        bool: (pow_sum == n)
    """
    p_adic = p_adic_expansion(n)
    pow_sum = sum(pow(coeff, power) for coeff in p_adic)
    result = (pow_sum == n)
    return result


def get_limit() -> int:
    """Returns the maximal number for which it is possible to write a number as its digit sum to the power 5, i.e. 10**n>n*9**5.

    Returns:
        int: limit
    """
    for n in itertools.count(1):
        if 10**n > n*9**5:
            result = 10**n
            return result


if __name__ == '__main__':
    result = main()
    print(result)
