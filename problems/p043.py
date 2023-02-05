import itertools
from functools import reduce


def interesting_substrings(pandigital: str) -> bool:
    '''
    Returns whether the pandigital satisfies the substring divisibility defined in https://projecteuler.net/problem=43
    '''

    PRIMES = [2, 3, 5, 7, 11, 13, 17]

    interesting_pandigital = (
        int(pandigital[k:k+3]) % PRIMES[k-1] == 0 for k in range(1, 8))
    result = reduce(lambda x, y: x and y, interesting_pandigital)

    return result


def main() -> None:
    '''We filter all possible pandigitals of the form 9876543210 
    with the interesting_substring function and sum the remaining ones.'''

    PANDIGITAL = '9876543210'

    pandigitals = (''.join(x) for x in itertools.permutations(PANDIGITAL))
    interesting_pandigitals = filter(interesting_substrings, pandigitals)
    result = sum(int(pandigital) for pandigital in interesting_pandigitals)

    print(result)



if __name__ == '__main__':
    main()
