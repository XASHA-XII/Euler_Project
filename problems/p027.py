import itertools
from typing import Tuple

from utils import is_prime_cached


'''
https://projecteuler.net/problem=27
Quadratic primes
'''

def main()->int:
    """Returns a*b where a,b maximize the functions n**2+a*n+b in the sense that its produces the most consequtive primes 
    for n=1,... under the constraint |a|,|b|<1000. We solve by brute-forcing.

    Returns:
        int: a*b 
    """
    N=1000
    A, B = range(-N, N), range(-N, N+1)
    a, b = max(itertools.product(A, B), key=quadratic_primes_series)
    result=a*b
    return result





def quadratic_primes_series(tuple:Tuple[int]):
    """For a given quadratic function of the form x**2+a*x+b for a,b integer returns the number of consecutive primes 
    generated from this function for x=1,...,n.

    Args:
        tuple (Tuple[int]): a,b coefficients in the function x**2+a*x+b

    Returns:
        _type_: number of consecutive primes
    """
    a,b=tuple
    for n in itertools.count():
        quadratic=n**2+a*n+b
        if not is_prime_cached(quadratic):
            return n


if __name__=='__main__':
    result=main()
    print(result)