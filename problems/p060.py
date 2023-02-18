'''
https://projecteuler.net/problem=60
Prime pair sets
'''

import itertools
import time
from typing import List

from utils import sieve_of_eratosthenes
from utils import is_prime_probabilistic


def has_prime_concats(primes: List[int], p: int):
    for q in primes:
        if not is_prime_probabilistic(int(f'{q}{p}')):
            return False
        elif not is_prime_probabilistic(int(f'{p}{q}')):
            return False
    return True




def main()->None:
    """Two variants to solve the problem. The nested loops version is much more efficient.
    """

    start= time.time()
    result = variant_1()
    end = time.time()
    print(f"Result {result} after {end-start} seconds with main.")


    start= time.time()
    result = variant_2()
    end = time.time()
    print(f"Result {result} after {end-start} seconds with main_alternative.")





def variant_1()->int:
    """Returns the minimal sum of primes satisfying the property in https://projecteuler.net/problem=60. 
    Uses the 5 nested loops function find_minimal_sequence.

    Returns:
        int: Minimal sum of primes.
    """
    for n in itertools.count():
        limit = 10_000*n
        result = find_minimal_prime_sum_loops(limit)
        if result == limit:
            print(f'No solution found for n = {limit}.')
            continue
        else:
            return result


def variant_2():
    """Returns the minimal sum of primes satisfying the property in https://projecteuler.net/problem=60. 
    Uses the functional approach find_minimal_sequence.

    Returns:
        _type_: _description_
    """
    SEQ_LEN=5
    for k in itertools.count(0,10_000):
        primes = sorted(list(sieve_of_eratosthenes(k)-{2,5}))
        print(k)
        new_limit=k
        result=k
        while new_limit is not None:
            new_limit=find_minimal_prime_sum_functional([],new_limit-1,primes,SEQ_LEN)
            if new_limit is not None:
                result=new_limit
        if result<k:
            break
    return result





def find_minimal_prime_sum_loops(limit: int) -> int:
    """Given a limit, this function checks if a prime sequence that satisfies the family property defined in https://projecteuler.net/problem=60
     and that has a sum of less than the limit exists. We naively loop through possible permutations of primes smaller than the initial limit.
     This list of primes is generated using the sieve of eratosthenes.

    Args:
        limit (int): Limit

    Returns:
        int: Minimal sum of primes.
    """
    prime_dict = sieve_of_eratosthenes(limit)-{2, 5}
    primes = sorted(list(prime_dict))
    num_of_primes = len(primes)
    for i in range(num_of_primes):
        single = [primes[i]]
        if sum(single) > limit / 5:
            break
        else:
            for j in range(i+1, num_of_primes // 4):
                tuple = single + [primes[j]]
                if sum(tuple) > 2*limit // 5:
                    break
                elif has_prime_concats(single, primes[j]):
                    for k in range(j+1, num_of_primes // 3):
                        triple = tuple + [primes[k]]
                        if sum(triple) > 3*limit // 5:
                            break
                        elif has_prime_concats(tuple, primes[k]):
                            for l in range(k+1, num_of_primes // 2):
                                quads = triple + [primes[l]]
                                if sum(quads) > 4*limit // 5:
                                    break
                                elif has_prime_concats(triple, primes[l]):
                                    for m in range(l+1, num_of_primes // 1):
                                        quints = quads+[primes[m]]
                                        if sum(quints) > limit // 1:
                                            break
                                        elif has_prime_concats(quads, primes[m]):
                                            limit = min(limit, sum(quints))
    return limit


def find_minimal_prime_sum_functional(index, limit, primes,seq_len):
    current_length = len(index)
    if len(index) == seq_len:
        return sum(primes[i] for i in index)
    else:

        start = index[-1] + 1 if (current_length >0) else 0 
        end = len(primes)
        current_sequence = [primes[i] for i in index]
        for k in range(start, end):
            current_prime = primes[k]
            if current_prime > limit:
                break
            elif not has_prime_concats(current_sequence, current_prime):
                continue
            else:
                index.append(k)
                next_sequence = find_minimal_prime_sum_functional(index, limit-current_prime,primes,seq_len)

                if next_sequence is not None:
                    return next_sequence

                index.pop()

  
        return None


                





if __name__ == '__main__':
    main()

