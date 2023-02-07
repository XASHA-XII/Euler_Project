from utils import sieve_of_eratosthenes


'''
https://projecteuler.net/problem=10
Summation of primes
'''


def main() -> None:
    '''Returns the sum of all primes below two million using the sieve of Eratosthenes.'''
    N = 2*10**6
    primes = sieve_of_eratosthenes(N)
    result = sum(primes)
    print(result)


if __name__ == '__main__':
    main()
