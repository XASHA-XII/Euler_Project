import unittest

from ..problems import p035
from ..problems.utils import sieve_of_eratosthenes


class TestP036(unittest.TestCase):
    def test_circular_shifts(self):
        # your test code here
        test_1 = p035.circular_shifts([1, 2, 3, 4])
        self.assertEqual(test_1, [[1, 2, 3, 4], [2, 3, 4, 1], [
                         3, 4, 1, 2], [4, 1, 2, 3]])

    def test_is_circular_prime(self):
        PRIMES = sieve_of_eratosthenes(1000)
        test_1 = p035.is_circular_prime(971, PRIMES)

        self.assertTrue(test_1)


if __name__ == '__main__':
    unittest.main()
