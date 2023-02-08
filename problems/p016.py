from utils import p_adic_expansion

def main()-> int:
    '''Returns the digit sum of 2**1000'''
    N=2**1000
    result=sum(p_adic_expansion(N))
    return result

if __name__=='__main__':
    result=main()
    print(result)