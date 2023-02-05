import unittest
import p033
from p033 import Fractions


class TestFractions(unittest.TestCase):

    def setUp(self) -> None:
        self.one_tenth = Fractions(1, 10)
        self.ten_hundredth = Fractions(10, 100)
        self.one_half = Fractions(1, 2)
        self.one_twentieth = Fractions(1, 20)
        self.x = Fractions(49, 98)
        self.y = Fractions(4, 8)

    def test_equal(self):

        self.assertEqual(self.one_tenth, self.ten_hundredth)
        self.assertNotEqual(self.one_tenth, self.one_half)
        self.assertEqual(self.x, self.y)

    def test_multiplication(self):

        product_1 = self.ten_hundredth*self.one_half
        product_2 = self.one_tenth*self.one_half

        self.assertEqual(product_1, self.one_twentieth)
        self.assertEqual(product_2, self.one_twentieth)

    def test_filter_values(self):
        self.assertTrue(p033.filter_values((49,98)))
        self.assertFalse(p033.filter_values((11,33)))
        self.assertFalse(p033.filter_values((10,30)))
        self.assertFalse(p033.filter_values((15,30)))


if __name__ == '__main__':
    unittest.main()
