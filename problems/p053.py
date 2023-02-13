from math import comb


'''
https://projecteuler.net/problem=53
Combinatoric selections
'''

def main() -> int:
    """Returns the number of binomial coefficients (n,r) for 1 <= n <= 100 that exceed 10**6.

    Returns:
        int: Number of binomial coefficients.
    """
    LIMIT = 10**6
    N = 100

    bigger_than_limit = 0
    for n in range(1, N+1):
        smaller_than_limit = 0
        for r in range(0, n+1):
            if comb(n, r) > LIMIT:
                bigger_than_limit = bigger_than_limit + \
                    (n+1 - smaller_than_limit)
                break
            else:
                smaller_than_limit += 2

    return bigger_than_limit


if __name__ == '__main__':
    result = main()
    print(result)
