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
    pass


if __name__ == '__main__':
    PANDIGITAL = '9876543210'
    
    pandigitals = (''.join(x) for x in itertools.permutations(PANDIGITAL))
    interesting_pandigitals = filter(interesting_substrings, pandigitals)
    result = sum(int(pandigital) for pandigital in interesting_pandigitals)
    print(result)

    # pandigital='1406357289'
    # PRIMES = [2, 3, 5, 7, 11, 13, 17]
    # for k in range(1,8):
    #     print(pandigital[k:k+3])
    #     print(PRIMES[k-1])

    # print(interesting_substrings(pandigital))

    # pandigitals = (''.join(x) for x in itertools.permutations(PANDIGITAL))
    # #interesting_pandigitals = filter(interesting_substrings, pandigitals)

    # for pandi in pandigitals:
    #     if pandi == pandigitals:
    #         print(pandi)
