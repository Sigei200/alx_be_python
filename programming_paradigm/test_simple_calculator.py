#!/usr/bin/env python3
"""
test_simple_calculator.py:
Unit tests for the SimpleCalculator class using the unittest framework.
"""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up a new SimpleCalculator instance before each test method.
        This ensures tests are independent and start from a clean state.
        """
        self.calc = SimpleCalculator()

    # --- Test methods for add() ---
    def test_addition_positive_numbers(self):
        """Test add method with two positive integers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_addition_negative_numbers(self):
        """Test add method with two negative integers."""
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_addition_mixed_numbers(self):
        """Test add method with positive and negative integers."""
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -3), 2)
        self.assertEqual(self.calc.add(-7, 2), -5)

    def test_addition_zero(self):
        """Test add method with zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(-8, 0), -8)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_float_numbers(self):
        """Test add method with floating-point numbers."""
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(-1.5, 2.0), 0.5)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3) # Use assertAlmostEqual for floats due to precision issues

    # --- Test methods for subtract() ---
    def test_subtract_positive_numbers(self):
        """Test subtract method with two positive integers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 20), -10) # Result is negative

    def test_subtract_negative_numbers(self):
        """Test subtract method with two negative integers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2) # -5 - (-3) = -5 + 3 = -2
        self.assertEqual(self.calc.subtract(-10, -20), 10)

    def test_subtract_mixed_numbers(self):
        """Test subtract method with positive and negative integers."""
        self.assertEqual(self.calc.subtract(5, -3), 8) # 5 - (-3) = 5 + 3 = 8
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtract_zero(self):
        """Test subtract method with zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract_float_numbers(self):
        """Test subtract method with floating-point numbers."""
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.subtract(10.3, 0.1), 10.2)

    # --- Test methods for multiply() ---
    def test_multiply_positive_numbers(self):
        """Test multiply method with two positive integers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_multiply_negative_numbers(self):
        """Test multiply method with two negative integers."""
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

    def test_multiply_mixed_numbers(self):
        """Test multiply method with positive and negative integers."""
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(5, -4), -20)

    def test_multiply_zero(self):
        """Test multiply method with zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, -10), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiply_float_numbers(self):
        """Test multiply method with floating-point numbers."""
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02)


    # --- Test methods for divide() ---
    def test_divide_positive_numbers(self):
        """Test divide method with two positive integers, exact division."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(100, 10), 10.0)

    def test_divide_negative_numbers(self):
        """Test divide method with two negative integers."""
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_mixed_numbers(self):
        """Test divide method with positive and negative integers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)

    def test_divide_by_zero(self):
        """Test divide method when denominator is zero."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Even 0/0 is None per the spec

    def test_divide_with_remainder(self):
        """Test divide method with division resulting in a float."""
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)

    def test_divide_zero_numerator(self):
        """Test divide method when numerator is zero and denominator is non-zero."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)

# This allows you to run the tests directly from the command line
if __name__ == '__main__':
    unittest.main()