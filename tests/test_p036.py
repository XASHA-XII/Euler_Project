import unittest

from ..problems import p036


class TestExample(unittest.TestCase):
    def test_is_palindrom(self):

        test_1 = p036.is_palindrom(585)
        test_2 = p036.is_palindrom(111)
        self.assertTrue(test_1)
        self.assertFalse(test_2)


if __name__ == '__main__':
    unittest.main()
