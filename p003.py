import itertools


def biggest_prime_factor(n: int) -> int:
    ''' Returns the biggest prime factor of a integer.'''
    if isinstance(n, int) and n not in {1, 2}:
        for p in itertools.count(2):
            if p**2 > n:
                return n
            elif (n % p == 0):
                n = n // p
    else:
        raise ValueError(
            "Zero and one do not have a prime factor decomposition")


def main() -> None:
    '''
    Returns the biggest prime factor of 600851475143.
    '''
    N = 600851475143
    print(f'{N}`s biggest prime factor is {biggest_prime_factor(N)}.')


if __name__ == '__main__':
    main()
