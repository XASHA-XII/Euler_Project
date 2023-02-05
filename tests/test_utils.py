import unittest

from ..problems import utils


class TestUtils(unittest.TestCase):

    def test_p_adic_expansion(self):
        test_1 = utils.p_adic_expansion(1000)

        self.assertEqual(test_1, [1, 0, 0, 0])

    def test_adic_inverse(self):
        test_1 = utils.p_adic_inverse([1, 2, 3])
        print(test_1)
        self.assertEqual(test_1, 123)

    def test_is_prime(self):
        test_0 = utils.is_prime(1)
        test_1 = utils.is_prime(5)
        test_2 = utils.is_prime(25)
        test_3 = utils.is_prime(26)

        self.assertFalse(test_0)
        self.assertTrue(test_1)
        self.assertFalse(test_2)
        self.assertFalse(test_3)

    def test_sieve_of_eratosthenes(self):
        test_1 = utils.sieve_of_eratosthenes(29)

        self.assertEqual(test_1, {2, 3, 5, 7, 11, 13, 17, 19, 23, 29})


if __name__ == '__main__':
    unittest.main()
