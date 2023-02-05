import math

from utils import p_adic_expansion

cache = {}
def factorial(x):
    return cache.setdefault(x, math.factorial(x))


def is_curious(n: int) -> bool:
    '''Returns whether a number is curious. For example 145 =1!+4!+5!=145'''
    if n < 0 or not isinstance(n, int):
        raise ValueError
    curious = sum(factorial(x) for x in p_adic_expansion(n))
    return curious == n

def compute_limit()->int:
    MAX_FACTORIAL = factorial(9)
    n = 1
    while 10**n < n*MAX_FACTORIAL:
        n += 1
    return 10**n



def main() -> None:
    '''Sum of curious numbers, 1 and 2 excluded.'''

    LIMIT=compute_limit()

    result = sum(filter(is_curious, range(3, LIMIT)))
    print(result)


if __name__ == '__main__':
    main()
