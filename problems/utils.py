import math
from typing import List


def p_adic_expansion(n: int, p: int = 10) -> List[int]:
    '''
    Returns the p-adic expansion of a number with respect to some basis p.
    Parameters:
        n (int):    The Number.
        p (int):    The base.
    Returns:
        List[int]   The p-adic expansion

    Example:
        n=1234, p = 10 -> [1,2,3,4] 

    '''
    assert (n > 0 and isinstance(n, int)) and (p > 0 and isinstance(p, int))
    expansion = []
    while n > 0:
        expansion.append(n % p)
        n //= p
    return list(reversed(expansion))


def p_adic_inverse(expansion: List[int]) -> int:
    '''
    The inverse of the p_adic expansion. Only the base p=10 is implemented.
    Parameters:
        expansion List[int]:    A p-adic expansion
    Returns:
        int
    Example:
    [1,2,3,4] -> 1234
    '''
    n = len(expansion)
    return sum((x * (10 ** (n-i-1)) for i, x in enumerate(expansion)))


def is_prime(n: int) -> bool:
    '''
    Returns whether a number is prime or not
    Parameters:
        n (int) number
    Returns:
        boolean: primness of the number
    '''
    assert isinstance(n, int)
    if n <= 1:
        return False
    LIMIT = int(math.sqrt(n))+1
    for k in range(2, LIMIT):
        if n % k == 0:
            return False
    return True


def sieve_of_eratosthenes(n: int) -> List[int]:
    '''
    Sieve of Eratosthenes. Returns all primes up to n.
    Parameters:
        n (int):    number
    Return:
        List of primes
    '''
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return set(p for p in range(2, n + 1) if primes[p])
