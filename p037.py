import itertools
from typing import List

from utils import p_adic_expansion, p_adic_inverse, is_prime


def truncate_list(lst: List[int])->List[List[int]]:
    '''
    Parameters:
    lst (List[int]): A list of integers.
    
    Returns:
    List[List[int]]: A list of sublists, each created by truncating the original list from either the left or the right end.
    '''
    right_to_left = [lst[:i] for i in range(1, len(lst))]
    left_to_right = [lst[i:] for i in range(len(lst))]
    return left_to_right + right_to_left


def is_truncatable_prime(n: int) -> bool:
    truncates = truncate_list(p_adic_expansion(n))
    truncated_primes = [p_adic_inverse(x) for x in truncates]
    return truncated_primes == list(filter(is_prime, truncated_primes))


def main() -> None:
    all_truncated_primes = filter(is_truncatable_prime, itertools.count(10))
    first_elven_truncated_primes = itertools.islice(
        filter(is_truncatable_prime, itertools.count(10)), 11)
    print(
        f'The sum of all truncatable primes equals the sum of the first eleven which is given by {sum(first_elven_truncated_primes)}.')


if __name__ == '__main__':
    #main()
    print(truncate_list([1,2,3,4]))
