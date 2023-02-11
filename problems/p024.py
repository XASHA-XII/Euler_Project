import itertools

'''
https://projecteuler.net/problem=24
Lexicographic permutations
'''


def main() -> str:
    '''Returns the millionth permutation of the string 0123456789 ordered lexicographically.
    By default, itertools.permutations generates the permutations in this order.'''
    POSITION = 10**6
    PERMUTATIONS = itertools.permutations(range(10))

    result = next(itertools.islice(PERMUTATIONS, POSITION-1, POSITION))
    result = ''.join(map(str, result))
    return result


if __name__ == '__main__':
    result = main()
    print(result)
