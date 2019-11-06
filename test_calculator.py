import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def test_one_add_one(self):
        calculator = Calculator()
        result = calculator.add(1, 1)
        self.assertEqual(2, result)


