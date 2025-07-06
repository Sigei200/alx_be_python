#!/usr/bin/env python3
"""
polymorphism_demo.py:
Demonstrates polymorphism and method overriding using a Shape base class
and derived Rectangle and Circle classes.
"""

import math

class Shape:
    """
    Base class for shapes.
    Defines an 'area' method that must be overridden by derived classes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by subclasses.
        Raises NotImplementedError if not overridden.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    Calculates its area based on length and width.
    """
    def __init__(self, length, width):
        """
        Initializes a Rectangle instance.

        Args:
            length (float or int): The length of the rectangle.
            width (float or int): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method from Shape to calculate the rectangle's area.
        Formula: length * width
        """
        return self.length * self.width

class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    Calculates its area based on radius.
    """
    def __init__(self, radius):
        """
        Initializes a Circle instance.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area method from Shape to calculate the circle's area.
        Formula: pi * radius^2
        """
        return math.pi * (self.radius ** 2)