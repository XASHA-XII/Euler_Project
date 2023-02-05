def sum_formula(n: int) -> int:
    '''Returns the sum of all numbers smaller or equal some integer n.'''
    if n < 0 or not isinstance(n,int):
        raise ValueError("Only postive integers are allowed")
    result = int(n*(n+1)//2)
    return result

def sum_square_formula(n: int) -> int:
    '''Returns the sum of all numbers smaller or equal some integer n.'''
    if n < 0 or not isinstance(n,int):
        raise ValueError("Only postive integers are allowd")
    result = int((n*(n+1)*(2*n+1))//6)
    return result


def main() -> None:
    '''Square of sum vs sum of squares.'''
    N=100
    result = sum_formula(N)**2-sum_square_formula(N)
    print(result)


if __name__ == '__main__':
    main()
