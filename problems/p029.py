import itertools

'''
https://projecteuler.net/problem=29
Distinct powers
'''

def main()->int:
    """Returns the number of distinct terms generated by the function f(a,b)=a**b for 2 <= a,b <= 100

    Returns:
        int: size of the image of the function.
    """
    N = 100
    A, B = range(2, N+1), range(2, N+1)
    distinct_terms = set(a**b for (a, b) in itertools.product(A, B))
    result=len(distinct_terms)
    return result

if __name__=='__main__':
    result=main()
    print(result)