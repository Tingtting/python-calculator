import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(2, 4), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(0, 1), 0)
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_devide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(5, 5), 1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)
        self.assertEqual(self.calc.modulo(15, 4), 3)

    
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()