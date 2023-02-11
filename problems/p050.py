import functools
import time

from utils import is_prime
from utils import sieve_of_eratosthenes


'''
https://projecteuler.net/problem=50
Consecutive prime sum
'''


def main() -> int:
    '''Computes the prime below 1 million that can be expressed as the longest sequence of primes.
    A possible optimization would be to generate a dictionary of primes to speed up the look up'''
    LIMIT = 10**6
    primes = sorted(list(sieve_of_eratosthenes(LIMIT)))
    num_of_primes = len(primes)

    global_best_sum = -1
    global_best_consec = -1

    for k in range(num_of_primes):
        sum_p = primes.pop(0)
        remaining_primes = (p for p in primes)
        for consec, prime in enumerate(remaining_primes):
            if sum_p + prime > LIMIT:
                break
            else:
                sum_p += prime
            if cached_is_prime(sum_p):
                local_best_consec = consec
                local_best_sum = sum_p
        if local_best_consec > global_best_consec:
            global_best_consec = local_best_consec
            global_best_sum = local_best_sum
            print(global_best_sum)

    result = global_best_sum
    return result


@functools.lru_cache(maxsize=None)
def cached_is_prime(p: int) -> bool:
    '''Returns whether a positive integer p is prime or not. Results are cached.'''
    return is_prime(p)


if __name__ == '__main__':
    start_time = time.time()
    result = main()
    print(result)

    end_time = time.time()
    print("Elapsed time: {:.2f} seconds".format(end_time - start_time))
