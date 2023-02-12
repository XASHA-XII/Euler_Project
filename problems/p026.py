import itertools
import functools

'''
https://projecteuler.net/problem=26
Reciprocal cycles
'''


def main() -> int:
    """Returns the integer n<=1000 that maximimizes the cyle length of fractions.

    Returns:
        int: the maximal cycle length
    """
    N = 1000
    cycle_length_num_fixed = functools.partial(cycle_length, 1)
    result = max(range(1, N), key=cycle_length_num_fixed)
    return result


def cycle_length(num: int, denum: int) -> int:
    """Returns the cycle length of fraction. For example,
        1/7 = 0.142857142857....=:0.(142857).
        Assumes denum > num.

    Args:
        num (int): positive integer, the  numerator
        denum (int): positive integer, the  denominator

    Returns:
        int: The length of the cycle, i.e. for 1/7 = len(142857)=6
    """
    numerators = {}
    for k in itertools.count():
        num = 10*(num % denum)
        if num in numerators:
            return k - numerators[num]
        else:
            numerators[num] = k


if __name__ == '__main__':
    result = main()
    print(result)
