import math

from utils import p_adic_expansion

'''
https://projecteuler.net/problem=20
Factorial digit sum
'''


def main()-> int:
    '''Computes the digit sum of 100!'''
    N=math.factorial(100)
    result=sum(p_adic_expansion(N))
    return result


if __name__=='__main__':
    result = main()
    print(result)