#!/usr/bin/env python3
"""
robust_division_calculator.py:
Contains the safe_divide function for robust division, handling
ZeroDivisionError and ValueError for non-numeric inputs.
"""

def safe_divide(numerator, denominator):
    """
    Performs division of two numbers, robustly handling potential errors.

    Args:
        numerator (str or float or int): The numerator for the division.
                                         Expected to be convertible to a number.
        denominator (str or float or int): The denominator for the division.
                                           Expected to be convertible to a number.

    Returns:
        str: An error message if division by zero or non-numeric input occurs.
        float: The result of the division if successful.
    """
    try:
        # Attempt to convert numerator and denominator to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        # Catch ValueError if conversion to float fails (non-numeric input)
        return "Error: Please enter numeric values only."

    try:
        # Attempt to perform division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        # Catch ZeroDivisionError if denominator is zero
        return "Error: Cannot divide by zero."
    except Exception as e:
        # A catch-all for any other unexpected errors, good for debugging
        return f"An unexpected error occurred: {e}"