from utils import sieve_of_eratosthenes, p_adic_expansion, p_adic_inverse


def circular_shifts(lst):
    return [lst[i:] + lst[:i] for i in range(len(lst))]


def is_circular_prime(n: int, primes) -> bool:
    '''Returns whether a prime is circular, i.e. it's numerals permuations are all primes:
    :param: n: circular candidate
    :param: primes, list of primes'''
    expansion = p_adic_expansion(n)
    shifts = set(p_adic_inverse(x) for x in circular_shifts(expansion))
    return shifts.issubset(primes)


def main() -> None:
    '''Circular primes below one million'''
    N = int(1e6)
    PRIMES = sieve_of_eratosthenes(N)
    circular_primes = [x for x in PRIMES if is_circular_prime(x, PRIMES)]
    print(
        f'Number of circular primes below one million: {len(circular_primes)}.')


if __name__ == '__main__':
    main()
