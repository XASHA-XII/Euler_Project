import itertools
from utils import is_prime

'''
https://projecteuler.net/problem=46
Goldbach's other conjecture
'''


def main() -> int:
    '''
    Returns the first odd composite positive integer that cannot be written
    as the sum of a prime and two times a square number. We loop through all odd composites.
    Then we loop through all square numbers smaller than a given odd composite and check if
    the remainder is prime. If this is not the case for any square number, we found the solutionF.
    '''
    odd_composites = (k for k in itertools.count(9, 2) if not is_prime(k))

    for oc in odd_composites:
        counter_example = True
        squares = (k**2 for k in range(1, oc+1))
        for sq in squares:
            p = oc-2*sq
            if is_prime(p):
                counter_example = False
                break
        if counter_example:
            result = oc
            return result


if __name__ == '__main__':
    result = main()
    print(result)
