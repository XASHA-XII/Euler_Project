from p004 import is_palindrom

'''
https://projecteuler.net/problem=55
Lychrel numbers
'''


def main() -> None:
    """Returns the number of integers below 10**4 that don't yield a palindrom
    by iteration x_{n+1}=x + reversed(x) after at most 50 iterations.

    Returns:
        _type_: _description_
    """
    N = 10**4
    result = sum(1 for n in range(1, N) if is_lychrel_number(n))
    return result


def is_lychrel_number(n: int) -> bool:
    """Checks the lychrelity of integers. We call numbers lychrel numbers if the iteration x_{n+1}=x + reversed(x)
    doesn't yield a palindrom after 50 iterations

    Args:
        n (int): lychrel number candiate
    Returns:
        bool: lychrelity
    """
    LIMIT = 50
    for _ in range(LIMIT+50):
        n = n + int(str(n)[::-1])
        if is_palindrom(n):
            return False
    return True


if __name__ == '__main__':
    result = main()
    print(result)
