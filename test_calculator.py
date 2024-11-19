import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 8), 13)

    def test_add2(self):
        self.assertEqual(self.calc.add(-7, -3), -10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(15, 5), 10)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(-12, -7), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 6), 24)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(18, 6), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(14, 5), 4)
        
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(21, 7), 0)

    # New test cases to detect bugs
    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide_with_remainder(self):
        self.assertEqual(self.calc.divide(7, 2), 3)

    def test_modulo_negative_b(self):
        self.assertEqual(self.calc.modulo(10, -3), 1)

if __name__ == '__main__':
    unittest.main()
