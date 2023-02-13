import math

'''
https://projecteuler.net/problem=32
Pandigital products
'''


def main() -> int:
    """Returns the sum of all numbers that has dividers that form a pandigital string.


    Returns:
        int: The sum of all pandigital products.
    """
    LIMIT = int(math.sqrt(987654321))+1
    result = sum(n for n in range(1, LIMIT) if is_pandigital_product(n))
    return result


def is_pandigital_product(n: int) -> bool:
    """Checks if a number is a pandigital product, i.e. are a permutation of 987654321. For example, 39*186=7254.

    Args:
        n (int): integer

    Returns:
        bool: product-pandigitality
    """
    PANDIGITAL = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for m in range(1, int(math.sqrt(n)+1)):
        if n % m == 0:
            pandigital_product_candidate = sorted(str(n) + str(n//m) + str(m))
            if pandigital_product_candidate == PANDIGITAL:
                return True
    return False


if __name__ == '__main__':
    result = main()
    print(result)
