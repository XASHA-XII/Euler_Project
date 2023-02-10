from functools import reduce
import itertools
from typing import Set, Tuple, List

from utils import sieve_of_eratosthenes

'''
https://projecteuler.net/problem=49
Prime permutations
'''


def main() -> int:
    '''The sequence 1487, 4817, 8147 is all primes and permutations of each other AND is a arithmetic sequence.
    This function returns the other 4 digit sequence of this kind in concatenated form, i.e. 148748178147 by filtering all
    four digits primes by
        1. if amongst permutations of the prime are atleast three primes
        2. if it contains a arithmetic sequence.'''
    N = 10**4
    primes = sieve_of_eratosthenes(N-1)
    candidates = set(p for p in primes if p > 1487)

    for p in candidates:
        prime_permutations = (candidates & permutations_of_int(p))
        if len(prime_permutations) >= 3:
            contains, subsequence = contains_arithmetic_subsequence(
                prime_permutations)
            if contains:
                result = ''.join(map(str, subsequence))
                return result


def permutations_of_int(p: int):
    '''Returns all permutations of an integer number.'''
    p_str = str(p)
    perms = set(''.join(p) for p in itertools.permutations(p_str))
    result = set(map(int, perms))
    return result


def contains_arithmetic_subsequence(st: Set) -> Tuple[bool, List[int]]:
    ''' Returns a tuple containing the boolean if the set contains an arithmetic subsequence
    of length 3 and the subsequence if it exists.'''
    lst = list(st)
    for x in lst:
        for y in (z for z in lst if z > x):
            z = (y-x+y)
            if z in lst:
                return True, [x, y, z]
    return False, []


if __name__ == '__main__':
    result = main()
    print(result)
