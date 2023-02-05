import unittest

from ..problems import p001 


class Testp001(unittest.TestCase):

    def test_ivisible_by_3_and_5(self):
        test_1 = p001.divisible_by_3_and_5(10)
        test_2 = p001.divisible_by_3_and_5(1000)

        self.assertEqual(test_1, 23)
        self.assertEqual(test_2, 233168)


if __name__ == '__main__':
    unittest.main()
