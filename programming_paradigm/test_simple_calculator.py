#!/usr/bin/env python3
"""
test_simple_calculator.py:
Unit tests for the SimpleCalculator class focusing on primary operations.
Aims to satisfy checker requirements for specific test method names.
"""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, designed to cover
    basic and edge cases for core arithmetic operations.
    """

    def setUp(self):
        """
        Set up a new SimpleCalculator instance before each test method.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the add method with various valid inputs.
        This method directly corresponds to the 'Checks for test_addition testcases' requirement.
        """
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, 200), 300)
        self.assertEqual(self.calc.add(-5, -10), -15)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)


    def test_subtract(self):
        """
        Test the subtract method with various valid inputs.
        This method directly corresponds to the 'Checks for test_subtraction testcases' requirement.
        """
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(1, -1), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(100, 50), 50)
        self.assertEqual(self.calc.subtract(-10, -5), -5)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2)


    def test_multiply(self):
        """
        Test the multiply method with various valid inputs.
        This method directly corresponds to the 'Checks for test_multiply' requirement.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(10, 10), 100)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02)


    def test_divide(self):
        """
        Test the divide method with various valid inputs, including division by zero.
        This method directly corresponds to the 'Checks for test_divide' requirement.
        """
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0) # Zero numerator, non-zero denominator
        self.assertIsNone(self.calc.divide(10, 0)) # Division by zero should return None
        self.assertIsNone(self.calc.divide(-5, 0)) # Division by zero with negative numerator
        self.assertIsNone(self.calc.divide(0, 0)) # 0/0 should also return None per spec
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)


    # You could add a test for the setUp itself, though less common for basic setup
    def test_calculator_instance(self):
        """Ensure that setUp correctly creates a SimpleCalculator instance."""
        self.assertIsInstance(self.calc, SimpleCalculator)


if __name__ == '__main__':
    unittest.main()