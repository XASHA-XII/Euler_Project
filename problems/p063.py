'''
https://projecteuler.net/problem=63
Powerful digit counts
'''

from math import log


def main() -> int:
    """Returns the number of all integers that have 5 digits and are fifth powers. For example 16807=7**5.
    We only need to check until a limit after which we have 9**n<10**(n-1).

    Returns:
        int: Number if five digits integers that are fifth powers.
    """
    LIMIT = int(log(10)/(log(10)-log(9)))+1
    result = 0
    for n in range(1, LIMIT+1):
        for num in range(1, 10):
            if len(str(num**n)) == n:
                result += 1
    return result


if __name__ == '__main__':
    result = main()
    print(result)
