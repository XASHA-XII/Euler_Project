from typing import List

from utils import sieve_of_eratosthenes


def main() -> int:
    '''
    Returns the first integer nummer starting from which, we have 4 numbers each having exactly 4 distinct prime factors.
    Example:
            134043=3*7*13*491
            134044=2**2*23*31*47
            134045=5*17*19*83
            134046=2*3**2*11*677.
    Using a variation of Sieve of Eratosthenes, we generate a list of the number of prime factors of 1,...,10**k 
    until we find the desired sequence. This leaves much room for improvement.'''
    DISTINCT = 4

    N = 10**1
    while True:
        dist_primes = distinct_primes(N)
        for k in range(N+2-DISTINCT):
            if dist_primes[k:k+DISTINCT] == [4, 4, 4, 4]:
                return k
        N *= 10


def find_sequence_of_distinct_primes(n: int, seq):
    '''Returns'''


def distinct_primes(n: int) -> List[int]:
    '''
    Variant of the Sieve of Eratosthenes. Returns the number distinct prime factors for all numbers less or equal to n.
    Parameters:
        n (int):    number
    Return:
        List of distinct prime factors
    Example
        distinc_prime(10)=[0,0,1,1,1,1,2,1,1]
    '''
    primes = [0 for i in range(n + 1)]
    p = 2
    while p <= n:
        if primes[p] == 0:
            for i in range(p, n + 1, p):
                primes[i] += 1
        p += 1
    return primes


if __name__ == '__main__':
    result = main()
    print(result)
