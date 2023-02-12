
'''
https://projecteuler.net/problem=28
Number spiral diagonals
'''

def main():
    '''Suppose all integers up to N are lined up spirally around 1. This function computes the sum of all corners. For example, for
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    we add up 1+3+5+7+9+13+17+21+25.
    In the upper right corner of the layers we always have square numbers 1,9,25,49,...
    '''
    N = 1001
    result = sum(4*k**2-6*k+6 for k in range(3, N+1, 2)) + 1
    return result


if __name__=='__main__':
    result=main()
    print(result)