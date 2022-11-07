import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_div_numbers(self):
        result = calc.div_numbers(10, 5)
        self.assertEqual(result, 2)