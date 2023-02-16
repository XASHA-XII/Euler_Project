import math
import functools
from typing import Tuple

from utils import p_adic_expansion


class Fractions(object):

    def __init__(self, num: int, denom: int) -> None:
        '''Returns fractions of integers where the denominator is not zero.'''
        if not (isinstance(num, int) and isinstance(denom, int)):
            raise ValueError('Numerator and denominator have to be integers.')
        if denom == 0:
            ZeroDivisionError
        else:
            self.num = num
            self.denom = denom

    def __str__(self) -> str:
        '''Override tostr by a / b'''
        return f"{self.num} / {self.denom}"

    def __eq__(self, other) -> bool:
        ''' a / b == c / d iff a*d=b*c
        '''
        return self.num*other.denom == self.denom*other.num

    def reduce(self) -> None:
        '''Reduces fraction, e.g. 2/4 = 1/2.'''
        gcd = math.gcd(self.num, self.denom)
        self.num = self.num // gcd
        self.denom = self.denom // gcd

    def __mul__(self, other):
        '''Overrides multiplication'''
        num = self.num * other.num
        denom = self.denom * other.denom
        product = Fractions(num, denom)
        product.reduce()
        return product

    def __add__(self,other):
        num= self.num*other.denom + other.num*self.denom
        denom=self.denom*other.denom
        result=Fractions(num,denom)
        result.reduce()
        return result


def filter_values(tuple: Tuple) -> bool:
    '''Filters the trivial examples e.g. 10/30 and 11/22'''
    if any(p % 10 == 0 or p % 11 == 0 for p in tuple):
        return False
    p, q = tuple
    p_expansion, q_expansion = p_adic_expansion(p), p_adic_expansion(q)
    if p_expansion[0] == q_expansion[1]:
        return Fractions(p, q) == Fractions(p_expansion[1], q_expansion[0])
    elif p_expansion[1] == q_expansion[0]:
        return Fractions(p, q) == Fractions(p_expansion[0], q_expansion[1])
    else:
        return False


def main() -> None:
    '''Finds equal fractions smaller than one that are equal if the last digit of numerator and denominator are canceled, e.g. 49/98 = 4/8. 
    Trivial examples are ignored.'''
    NUMS_AND_DENOMS = [(x, y) for x in range(10, 100)
                       for y in range(10, 100) if x < y]
    curious_fractions = filter(filter_values, NUMS_AND_DENOMS)
    curious_fractions = map(lambda x: Fractions(*x), curious_fractions)
    product_of_fractions = functools.reduce(
        lambda a, b: a*b, curious_fractions)
    print(
        f'The denominator of the curious fractions is given by {product_of_fractions.denom}')


if __name__ == '__main__':
    main()


