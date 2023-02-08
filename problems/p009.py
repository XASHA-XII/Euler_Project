'''
https://projecteuler.net/problem=9

Special Pythagorean triplet
'''


def main()->int:
    '''Returns the unique integer pythagorean triplet with a+b+c=1000,
        i.e. the solution of the equation system
                a**2+b**2=c**2
                a+b+c=1000
    '''
    N=1000
    for a in range(1,N):
        for b in range(a,N-a):
            c=N-a-b
            if a**2 + b**2 == c**2:
                return a*b*c
    return -1



if __name__=='__main__':
    result=main()
    print(result)