

def main():
    ''' Returns the product of the d_1,d_10,...,d_1_000_000 positions of the Champernowe number that concats all integer numbers,
    0.1234567891011...'''
    N = 6
    LIMIT = (10**N) // 2 + 9
    CHAMPERNOWE = "".join(str(i) for i in range(1, LIMIT))

    result = 1
    for k in range(N+1):
        result *= int(CHAMPERNOWE[10**k - 1])
    print(result)


if __name__ == '__main__':
    main()
