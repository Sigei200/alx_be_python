#!/usr/bin/env python3
"""
class_static_methods_demo.py:
Demonstrates the use and differences between class methods and static methods
in a Calculator class.
"""

class Calculator:
    """
    A class to demonstrate static and class methods.
    Includes a class attribute, a static method for addition,
    and a class method for multiplication.
    """
    # Class Attribute: Accessible by class methods and typically by instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Returns the sum of two numbers.
        Does not access instance-specific data (self) or class-specific data (cls).
        Behaves like a regular function, but logically belongs to the class.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Returns the product of two numbers.
        Takes 'cls' as its first parameter, allowing it to access class attributes
        like 'calculation_type'.
        """
        # Accessing the class attribute using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b