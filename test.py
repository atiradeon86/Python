"""
calculator -modul
Calculator - class
    sum(a,b) -> int : sum == a+b
"""

import unittest
from calculator import Calculator

class BasicCalcTests(unittest.TestCase):
    def test_sum_of_2(self):
        calc = Calculator()
        calc.sum(2,3)
        result = calc.sum(2,3)
        self.assertEqual(5, result)
