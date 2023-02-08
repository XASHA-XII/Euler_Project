import functools

'''
https://projecteuler.net/problem=14
Longest Collatz sequence
'''


def main() -> int:
    N = 10**6
    result = max(range(1, N), key=collatz_sequence)
    return result


@functools.cache
def collatz_sequence(n: int) -> int:
    '''Returns the length of the Collatz sequence starting at positive integer.'''
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            n_plus_one = n // 2
        else:
            n_plus_one = 3*n + 1
        return collatz_sequence(n_plus_one)+1


if __name__ == '__main__':
    result = main()
    print(result)
