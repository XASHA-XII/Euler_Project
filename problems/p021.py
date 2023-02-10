from math import isqrt


'''
https://projecteuler.net/problem=21
Amicable numbers
'''


def main() -> int:
    '''Returns the sum of all amicable below 10000'''
    N = 10**4
    result = sum(n for n in range(1, N) if is_amicable(n))

    return result


def is_amicable(n: int) -> bool:
    '''Checks whether a positive integer n is one part of a pair ofamicable numbers. 
    This means that if d(n) denotes the sum of all proper divisors of n (n itself excluded)
    that n=d(d(n)) and n!= d(n).
     '''
    m = sum_of_divisors(n)
    result = (n == sum_of_divisors(m)) and not (m == n)
    return result


def sum_of_divisors(n: int) -> int:
    '''Returns the sum of all proper divisors of a positive integer. In the formula 1 is added 
    because we skip one in the summation. Furthermore, we have to subtract sqrt(n) if n is a perfect square.'''
    if n == 1:
        return 1
    else:
        LIMIT = isqrt(n)
        result = sum(k + n//k for k in range(2, LIMIT+1) if n % k == 0) + 1
        if LIMIT**2 == n:
            result -= LIMIT

        return result


if __name__ == '__main__':
    result = main()
    print(result)
