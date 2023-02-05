import itertools

from utils import is_prime


def main()->None:
    '''
    Compute the largest pandigital number that is also a prime. An example is 2143. Hence, we may ignore pandigitals of the form "23" and "234".
    '''
    PANDIGITAL = '123456789'

    max_= -1
    for k in range(10,3,-1):
        n_pandigitals= (int(''.join(x)) for x in itertools.permutations(PANDIGITAL[:k]))
        try:
            max_=max(filter(is_prime,n_pandigitals))
            break
        except:
            pass
    print(max_)


if __name__=='__main__':
    main()