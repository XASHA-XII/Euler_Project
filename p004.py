import itertools
import functools

from utils import p_adic_expansion

@functools.cache
def is_palindrom(n: int) -> bool:
    '''Returns wheter the input is a palindrom or not
    :param n int: positive integer
    :return bool: 
    '''
    assert n > 0 and isinstance(n, int)
    expansion = p_adic_expansion(n)
    result = expansion == list(reversed(expansion))
    return result


def main() -> None:
    '''Returns the maximum palidrom that can be written as the product of two 3 digit numbers
    '''
    A=range(100,1000)
    result=max((k*l for k,l in itertools.product(A,A) if is_palindrom(k*l)))
    print(result)


if __name__ == '__main__':
    main()
