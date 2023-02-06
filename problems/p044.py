import math
import itertools
import functools

'''https://projecteuler.net/problem=44

P(k) = k * (3*k-1) // 2
'''


@functools.cache
def pentagon_number(n: int) -> int:
    '''Computes the n-th pentagon number for n>=1'''
    result = n*(3*n-1)//2
    return result


def is_pentagon_number(k: int) -> bool:
    '''Checks whether a number is a pentagon number, i.e. if k=n(3n-1)/2 for a integer number n. This is equivalent to
    n= (1 + sqrt(1+24*k))/6 being an integer number.
    '''
    interim_result = math.isqrt(1+24*k)
    if interim_result**2 == 1+24*k:
        result = ((1 + interim_result) % 6 == 0)
    else:
        result = False
    return result


def find_first_solution() -> int:
    '''Finds D= P_k-p_l such that P_k, P_l, P_k-p_l and P_k+p_l are all pentagon numbers'''
    for k in itertools.count():
        p_k = pentagon_number(k)
        for l in range(1, k):
            p_l = pentagon_number(l)
            if is_pentagon_number(p_k+p_l) and is_pentagon_number(p_k-p_l):
                result = p_k - p_l
                return result, k


def lower_limit(k: int, D: int):
    '''Given k,D this function solves the equation 
                P(k)-P(k-x)= D
       for x. Here, D= P(i)-P(j) for some i,j that is the solution of the previous function.
       The purpose of this function is, given a pentagonal number P(k) to the smallest possible P(k-x) that might be 
       a smaller solution than D. In this way, the main function stays O(n).      
    '''
    result = k - (int(1/6 * (-math.sqrt(-24*D+36*k**2-12*k+1) + 6*k-1)) + 1)
    return result


def main() -> None:
    ''' Given the solution in find_first_solution(), we check whether there is a smaller solution to the problem.'''
    result, N = find_first_solution()
    for k in itertools.count(N):
        p_k = pentagon_number(k)
        lower_lim = lower_limit(k, result)
        if p_k - pentagon_number(lower_lim) > result:
            break
        else:
            for l in range(lower_lim, k):
                p_l = pentagon_number(l)
            if is_pentagon_number(p_k+p_l) and is_pentagon_number(p_k-p_l):
                D = p_k-p_l
                result = min(result, D)

    print(result)


if __name__ == '__main__':
    main()
