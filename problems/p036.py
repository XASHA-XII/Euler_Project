from utils import p_adic_expansion
import time


def is_palindrom(n: int) -> None:
    '''Returns whether a positive integer is a palindrom in base 2 and 10.'''
    p_adic2 = p_adic_expansion(n, 2)
    p_adic10 = p_adic_expansion(n, 10)
    base2 = (p_adic2 == list(reversed(p_adic2)))
    base10 = (p_adic10 == list(reversed(p_adic10)))
    return base2 and base10


def main() -> None:
    '''Sums all positve integers that are palindromes both in base 2 and 10.'''
    N = int(1e6)
    result = sum([n for n in range(1, N) if is_palindrom(n)])
    print(result)


if __name__ == '__main__':

    start = time.time()

    main()

    end = time.time()
    print(f'Time elapsed: {end-start}.')
