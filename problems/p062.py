'''
https://projecteuler.net/problem=62
Cubic permutations
'''


import itertools
from typing import Generator


def main() -> int:
    """Returns the minimal cubic number, i.e. n=m**3 for some integer m, who has at least five permutations that are also cubic numbers.

    Returns:
        int: The minimal cubic number with five cubic permutations
    """
    for k in itertools.count(5):
        result = check_k_digit_cubes(k, 5)
        if result is not None:
            break
    return result


def check_k_digit_cubes(k: int, seq_len: int) -> int:
    """Checks if in the range of 10^k and 10^(k+1) is a cubic sequence of a given length. If none exists it returns zero.
    Otherwise it returns the minimal solution.

    Args:
        k (int): The exponent that defines the range in which to look for a solution.
        seq_len (int): The length of the cubic sequence

    Returns:
        int: None or the minimal element of the cubic sequence.
    """
    print(f"Checking cubic numbers between 10^{k} and 10^{(k+1)}")
    k_digits_cubes = sorted(list(gen_possible_cube_perms(10**(k))))
    while k_digits_cubes != []:
        cube = k_digits_cubes.pop(0)
        cubic_permutations = 1
        for i, other_cube in enumerate(k_digits_cubes):
            if sorted(cube) == sorted(other_cube):
                k_digits_cubes.remove(other_cube)
                cubic_permutations += 1
            if cubic_permutations == seq_len:
                return cube
            else:
                continue
    return None


def gen_possible_cube_perms(n: int) -> Generator[str, None, None]:
    """Yields the cubic numbers of the same digit length as the input number n as strings.

    Args:
        n (int): integer with k digits

    Yields:
        Generator[str, None, None]: Yields cubes for all integers with the same digits as n.
    """
    digits = len(str(n))
    lower_bound = int(pow(10, (digits-1)/3))
    upper_bound = int(pow(10, (digits)/3))
    for k in range(lower_bound, upper_bound+1):
        yield str(k**3)


if __name__ == '__main__':
    result = main()
    print(f'The solution is given by {result}.')
