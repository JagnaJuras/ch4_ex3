import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_div_numbers(self):
        result = calc.div_numbers(10, 5)
        self.assertEqual(result, 2)
        
    def test_mul_numbers(self):
        result = calc.mul_numbers(10, 5)
        self.assertEqual(result, 50)
