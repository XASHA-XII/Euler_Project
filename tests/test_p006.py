import unittest
from ..problems import p006


class Testp004(unittest.TestCase):

    def test_sum_formula(self):
        result = p006.sum_formula(10)

        self.assertEqual(result, 55)

    def test_sum_square_formula(self):
        result= p006.sum_square_formula(10)

        self.assertEqual(result,385)


if __name__ == '__main__':
    unittest.main()
