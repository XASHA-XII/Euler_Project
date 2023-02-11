import functools
import itertools


@functools.cache
def fibonacci(n:int)->int:
    if not isinstance(n,int) or n < 0:
        raise ValueError('Fibonacci numbers are only defined for positve integers.')
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main()-> int:
    '''Returns the first Fibonacci number that surpasses 10**999.'''
    LIMIT=10**999
    n=0

    fibonaccis=(fibonacci(n) for n in itertools.count())
    for n, fib in enumerate(fibonaccis):
        if fib>LIMIT:
            result=n+1 # in our notation F_0=1
            break
        
    return result


if __name__=='__main__':
    result = main()
    print(result)