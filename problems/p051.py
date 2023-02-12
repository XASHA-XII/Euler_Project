import functools
import itertools
from typing import Set

from utils import is_prime
from utils import sieve_of_eratosthenes


def main() -> int:
    """Returns the smallest p-valued prime familty of length 8.

    Returns:
        int: A prime number.
    """
    for k in itertools.count(4):
        N = 10**k
        primes = sorted(list(sieve_of_eratosthenes(N)))
        for p in primes:
            p_valued_family = prime_family(p, CARDINALITY=8)
            if p_valued_family:
                return min(p_valued_family)


def prime_family(p: int, CARDINALITY: int = 8) -> Set[int]:
    """Given a prime number p and a cardinality, this function returns a p-valued family of this cardinality if it exists. 
    Otherwise it returns an empty set.

    Args:
        p (int): A prime number
        CARDINALITY (int, optional): The length of families we are looking for. Defaults to 8.

    Returns:
        Set[int]: p-valued family of a given cardinality or an empty set.
    """
    p_str = str(p)
    distinct_digits = set(digit for digit in p_str)
    for digit in distinct_digits:
        p_str_wildcard = p_str.replace(digit, '*')
        p_valued_family = set()
        for k in range(10):
            p_member_str = p_str_wildcard.replace('*', f'{k}')
            p_member_int = int(p_member_str)
            if len(p_member_str) == len(str(p_member_int)):
                if cached_is_prime(p_member_int):
                    p_valued_family.add(p_member_int)
        if len(p_valued_family) >= CARDINALITY:
            return p_valued_family
    return set()


@functools.lru_cache(maxsize=None)
def cached_is_prime(p: int) -> bool:
    """Returns whether a positive integer p is prime or not. Results are cached.

    Args:
        p (int): A positive integer.

    Returns:
        bool: The primality of p.
    """
    ''''''
    return is_prime(p)


if __name__ == '__main__':
    result = main()
    print(result)
