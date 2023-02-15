import itertools

from utils import p_adic_expansion
'''
https://projecteuler.net/problem=56
Powerful digit sum
'''


def main():
    """Returns the maximal digit sum of a integer of the form a**b for 0<a,b<100.

    Returns:
        _type_: maximal digit sum
    """
    X = list(range(1, 100))
    result = max(sum(p_adic_expansion(a**b))
                 for a, b in itertools.product(X, X))
    return result


if __name__ == '__main__':
    result = main()
    print(result)
