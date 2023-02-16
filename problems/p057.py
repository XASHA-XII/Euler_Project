from p033 import Fractions


'''
https://projecteuler.net/problem=57
Square root convergents
'''


def main() -> int:
    """Returns the number of times the numerator has more digits than the denominator 
    in the fraction of sqrt(2)=1 / ( 1+ 1 /(1+sqrt(2))). This leads to an iteration of the form
    1 + x_n where x_{n+1}= 1 / ( 2 + x_n). Writing the right-hand side in fractional form, we have
    n / m = m / (2*m+n)

    Returns:
        int: number of times the numerator digits exceed the denominator digits in the first 1000 iterations.
    """
    N = 1000
    result = 0
    x = Fractions(1, 2)
    for k in range(2, N+1):
        x = Fractions(x.denom, 2*x.denom+x.num)
        approx = Fractions(1, 1)+x
        if len(str(approx.num)) > len(str(approx.denom)):
            result += 1
    return result


if __name__ == '__main__':
    result = main()
    print(result)
