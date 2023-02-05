def integer_solutions(n):
    '''
    Returns the number of integer solutions of a^2+b^2=c^2
    subject to the condition a+b+c=n
     '''
    result = 0
    for b in range(1, n+1):
        for a in range(1, b):
            c = n-a-b
            if a < b < c and a**2+b**2 == c**2:
                result += 1
    return result


def main() -> None:
    '''Returns the number n below 1000 that maximizes the integer solutions of a^2+b^2=c^2,
    subject to the condition a+b+c=n'''
    N = 1000
    result = max(range(1, N+1), key=integer_solutions)
    print(result)


if __name__ == '__main__':
    main()
