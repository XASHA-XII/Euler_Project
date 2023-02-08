import math

'''
https://projecteuler.net/problem=15
Lattice paths
'''


def main():
    '''
    Returns all distinct possible routes in a 20x20 grid, that start at (0,0) and end in (23,23).
    where only right and down moves are allowed. A route of this form is always formed by 20 down moves
    and 20 right moves. There are 40 over 20 possible routes.
    '''
    result = math.comb(40, 20)
    return result


if __name__ == '__main__':
    result = main()
    print(result)
