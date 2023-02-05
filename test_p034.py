import unittest
import math
import p034

class TestP034(unittest.TestCase):
    def test_is_curious(self):
        # test the factorial of 0
        result = p034.is_curious(145)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()