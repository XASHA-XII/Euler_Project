import unittest
import p004


class Testp004(unittest.TestCase):

    def test_is_palindrom(self):
        test_1 = p004.is_palindrom(10501)
        test_2 = p004.is_palindrom(10551)

        self.assertTrue(test_1)
        self.assertFalse(test_2)


if __name__ == '__main__':
    unittest.main()
