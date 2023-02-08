from math import log

from utils import sieve_of_eratosthenes

'''https://projecteuler.net/problem=7'''

def main()->None:
    '''Returns the 10001st prime using the sieve of Eratosthenes method. Very lazy solution:
    By the prime number theorem 
    https://en.wikipedia.org/wiki/Prime_number_theorem
    the n-th prime satisfies p_n< n*(log n + log log n).
    '''
    N=10001
    BOUND=int(N*(log(N)+ log(log(N))))+1

    primes=sorted(list(sieve_of_eratosthenes(BOUND)))
    result= primes[10000]
    print(result)



if __name__=='__main__':
    main()