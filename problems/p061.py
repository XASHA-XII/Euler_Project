'''
https://projecteuler.net/problem=61
Cyclical figurate numbers
'''


import itertools
from typing import List, Tuple


def main() -> int:
    """Returns the sum of the only ordered four digit cyclical set that consists of exactly one triangle, 
    square, pentagonal, hexagonal, heptagonal and octagonal number. An example of a cyclical set is 8129, 8281, 2882 where
    the next numbers first two digits are identical to the previous last two digits (this is also the case for the last and the first element).

    Returns:
        int: Sum of the cycical set.
    """
    LOWER = 1000
    UPPER = 9999
    def TRIANGLE(n): return n*(n+1)//2
    def SQUARE(n): return n**2
    def PENTA(n): return n*(3*n-1)//2
    def HEXA(n): return n*(2*n-1)
    def HEPTA(n): return n*(5*n-3)//2
    def OCTO(n): return n*(3*n-2)

    triangle = [TRIANGLE(n) for n in range(
        1, 200) if LOWER <= TRIANGLE(n) <= UPPER]
    square = [SQUARE(n) for n in range(1, 200) if LOWER <= SQUARE(n) <= UPPER]
    penta = [PENTA(n) for n in range(1, 200) if LOWER <= PENTA(n) <= UPPER]
    hexa = [HEXA(n) for n in range(1, 200) if LOWER <= HEXA(n) <= UPPER]
    hepta = [HEPTA(n) for n in range(1, 200) if LOWER <= HEPTA(n) <= UPPER]
    octo = [OCTO(n) for n in range(1, 200) if LOWER <= OCTO(n) <= UPPER]

    perms = itertools.permutations(
        (triangle, square, penta, hexa, hepta, octo))

    for perm in perms:
        result = search_cycle(*perm)
        if result is not None:
            return result

    return None


def search_cycle(triangle: List[int], square: List[int], penta: List[int], hexa: List[int], hepta: List[int], octo: List[int]) -> int:
    """Given six lists, this function searches for a cyclical sequence in those lists. If none exists, None is returned.
    In any loop all elements of the next loop all start with the last two digits of the previous loop. For example, 
    for tri=8281 all elements sq are in the range (8100,8199). 

    Returns:
        int: Sum of the cycical sequence found. None if no such sequence exists.
    """
    for tri in triangle:
        lower, upper = bounds_for_next_sequent(tri)
        for sq in [x for x in square if lower <= x <= upper]:
            lower, upper = bounds_for_next_sequent(sq)
            for pnt in [x for x in penta if lower <= x <= upper]:
                lower, upper = bounds_for_next_sequent(pnt)
                for hex in [x for x in hexa if lower <= x <= upper]:
                    lower, upper = bounds_for_next_sequent(hex)
                    for hep in [x for x in hepta if lower <= x <= upper]:
                        lower, upper = bounds_for_next_sequent(hep)
                        for oc in [x for x in octo if lower <= x <= upper]:
                            if oc % 100 == tri // 100:
                                result = sum([tri, sq, pnt, hex, hep, oc])
                                return result


def bounds_for_next_sequent(num: int) -> Tuple[int]:
    """Given a integer 1000<=n<=9999 returns the lower and upper bound of the n-hundreth numbers. For example for n=2563 it returns 2500 and 2599

    Args:
        num (int): four digit integer

    Returns:
        Tuple[int]: lower and upper bound
    """
    lower = (num % 100)*100
    upper = lower + 99
    return lower, upper


if __name__ == '__main__':
    result = main()
    print(f"The sum is given by {result}.")
