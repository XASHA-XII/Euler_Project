'''
https://projecteuler.net/problem=48
Self powers
'''


def main() -> int:
    '''Returns the last 10 digits of the sum 1**1+...+1000**1000.'''
    N=10**10
    result = sum(pow(k,k,N) for k in range(1, 1001)) % N
    return result


if __name__ == '__main__':
    result = main()
    print(result)
