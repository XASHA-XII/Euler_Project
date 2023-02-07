import itertools
from math import isqrt

'''
https://projecteuler.net/problem=45
Triangular, pentagonal, and hexagonal
Triangular:     T(n)=n(n+1)/2
Pentagonal:     P(n)=n(3n-1)/2
HexagonaL:      H(n)=n(2n-1)
'''



def hexagonal(n: int) -> int:
    '''Returns the n-th hexagonal number.'''
    H_n = n * (2*n - 1)
    return H_n

def is_pentagonal(x: int) -> int:
    '''
    Returns whether x is a pentagonal number, i.e.  
            x= (n * (3*n - 1)) // 2.
    This is verified by taking the inverse function
            n= 1/6 (1 + sqrt(1 + 24*x))
    and checking whether all terms involved are integer.
    '''
    interim_result = isqrt(1 + 24*x)
    if (interim_result**2 == 1 + 24*x):
        result = ((1 + interim_result) % 6 == 0)
    else:
        result = False
    return result


def main() -> int:
    '''Returns the second number that is triangular, pentagonal and hexagonal by looping through
     all hexagonal numbers and checking if they're triangular and pentagonal. The first such number is
     H(143)=40755.
     Since T(2m-1) = 2m*(2m-1) = H(n) 
     all hexagonal numbers are triangular numbers and we do not need to check them.
     '''

    N = 144
    for H_n in (hexagonal(k) for k in itertools.count(N)):
        if is_pentagonal(H_n):
            result = H_n
            return result


if __name__ == '__main__':
    result = main()
    print(result)
