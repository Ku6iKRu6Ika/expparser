import unittest
import math
from decimal import Decimal
from expparser.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test(self):
        c = Calculator()

        self.assertEqual(c.calc('2 + 2 * 2'), 6)
        self.assertEqual(c.calc('-2 + 2'), 0)
        self.assertEqual(c.calc('2 * (5 + 1)'), 12)
        self.assertEqual(c.calc('(2 + 5^2)^2'), 729)
        self.assertEqual(c.calc('2.5 + (0.1 * 100) / 2'), 7.5)
        self.assertEqual(c.calc('2(2 + 2.5)'), 9)
        self.assertEqual(c.calc('0 * 1'), 0)
        self.assertEqual(c.calc('log10(100)'), 2)
        self.assertEqual(round(c.calc('2 * PI'), 5), round(Decimal(2 * math.pi), 5))
        self.assertEqual(c.calc('(5^2 + 8 * (111 + 8.5 - 1) + 1) + (2122^0 + 1^999) - 1'), 975)
        self.assertEqual(c.calc('-(-(-2 - 99)) - 8'), -109)
        self.assertEqual(c.calc(' 7 / 4'), 1.75)
        self.assertEqual(c.calc(' 7 / 4 / (2 * 8 / 2)'), 0.21875)
        self.assertEqual(c.calc('-1 - (-1)'), 0)
        self.assertEqual(c.calc('5 % 2'), 1)
        self.assertEqual(c.calc('(7 * 7)^3 % 15'), 4)


if __name__ == '__main__':
    unittest.main()