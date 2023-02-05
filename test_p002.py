import unittest
import p002


class TestP0032(unittest.TestCase):

    def test_fibonacci(self):
        test_list = [p002.fibonacci(x) for x in range(1, 10)]
        first_ten_fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55]

        self.assertEqual(test_list, first_ten_fibs)


if __name__ == '__main__':
    unittest.main()
