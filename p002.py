import itertools
import functools


@functools.cache
def fibonacci(n: int) -> int:
    '''Returns the n-th Fibonacci number starting with 1.'''
    if isinstance(n, int) and n > 0:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    else:
        raise ValueError('Value is not a positive integer')


def main() -> None:
    '''Sums the all even valued Fibonaccis below 4 million. Even valued Fibonaccis are every third number starting with 2.'''
    LIMIT = int(4e6)
    sum_of_fibs = 0
    for n in itertools.count(2,3):
        fib = fibonacci(n)
        if fib < LIMIT and (fib % 2 == 0):
            sum_of_fibs += fib
        else:
            break
    print(sum_of_fibs)


if __name__ == '__main__':
    main()
