from typing import List

'''
https://projecteuler.net/problem=31
Coin sums
'''


def main() -> int:
    '''Returns the number of different ways 200 can be the result of combinations of [1, 2, 5, 10, 20, 50, 100, 200]. 
    This can be computed by first computing all prior interm results.'''
    COINS = [1, 2, 5, 10, 20, 50, 100, 200]
    result = dynamical_programm(COINS)
    return result[-1]


def dynamical_programm(base: List[int]) -> List[int]:
    '''Given a sorted list of base numbers, this function returns the number of possible ways 
    to get the numbers between base[0] and base[-1] by adding up base numbers.'''
    start,  end = base[0], base[-1]
    result = (end + 1) * [0]
    result[0] = 1
    for x in base:
        for y in range(start, end+1):
            if y >= x:
                result[y] += result[y-x]
    return result


if __name__ == '__main__':
    result = main()
    print(result)
