import unittest
import p003


class TestP0032(unittest.TestCase):

    def test_biggest_prime_factor(self):
        test_1 = p003.biggest_prime_factor(13195)

        self.assertEqual(test_1, 29)


if __name__ == '__main__':
    unittest.main()
