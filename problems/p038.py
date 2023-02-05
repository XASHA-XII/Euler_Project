def main() -> None:
    '''
    Computes the maximal pandigital number (i.e. perumations of 123456789)
    that can be written as the concatination of 1*x+2*x+...+n*x, where n>=2
    and x is a positve integer. For example
    1*192 2*192 3*192 = 192 384 576.
    '''
    LIMIT = int(1e6)
    retn = '192384576'
    for k in range(LIMIT):
        pan = str(k)
        for n in range(2, 10):
            pan += str(k*n)
            if ''.join(sorted(pan)) == '123456789':
                retn = max(retn, pan)
            elif len(pan) > 9:
                break

    print(retn)


if __name__ == '__main__':
    main()
