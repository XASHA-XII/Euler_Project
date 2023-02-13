import itertools

'''
https://projecteuler.net/problem=52
Permuted multiples
'''


def main() -> int:
    """Returns the first number x such that 2*x,...,6*x has the same digits, only permuted.

    Returns:
        int: The result.
    """
    for n in itertools.count(1):
        multiplied_digits = sum(1 for mult in range(
            2, 7) if same_digits(n, mult*n))
        if multiplied_digits == 5:
            result = n
            return result


def same_digits(n: int, m: int) -> bool:
    """Checks if two integers contain the same digits.

    Args:
        n (int): number
        m (int): number

    Returns:
        bool: same-digitality
    """
    result = sorted(str(n)) == sorted(str(m))
    return result


if __name__ == '__main__':
    result = main()
    print(result)
