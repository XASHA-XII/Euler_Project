import itertools
from math import isqrt

from p006 import sum_formula as triangular


'''
https://projecteuler.net/problem=12
Highly divisible triangular number
Triangular numbers satisfy T_n= 1+...+n = n*(n+1) /2.
'''


def num_divisors(n: int) -> int:
    '''Returns the numbers of divisors of a integer n. 1 and n inclusive. 
    If n % k = 0 then n =k*l for some l. If l not k then we add two divisors.
    Furthermore, l >= sqrt(n)'''
    result = sum(2 for k in range(1, isqrt(n)+1) if n % k == 0)
    if isqrt(n)**2 == n:
        result -= 1
    return result


def main() -> int:
    '''Returns the first triangular number that has more than 500 divisors.'''
    for T_n in (triangular(n) for n in itertools.count(1)):
        if num_divisors(T_n) > 500:
            return T_n


if __name__ == '__main__':
    result = main()
    print(result)
