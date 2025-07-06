#!/usr/bin/env python3
"""
book_class.py:
Implements a Book class demonstrating Python magic methods:
__init__ (constructor), __del__ (destructor),
__str__ (string representation), and __repr__ (official representation).
"""

class Book:
    """
    Represents a book with a title, author, and publication year,
    and custom behavior through magic methods.
    """
    def __init__(self, title, author, year):
        """
        Constructor: Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        # print(f"Book '{self.title}' created.") # Optional: for internal debugging

    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed.
        Prints a message indicating the book being deleted.
        """
        # print("Inside __del__") # Optional: for internal debugging
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation: Returns a user-friendly string for the book.
        Used by print(), str(), and format().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Returns a string that could recreate the object.
        Used by repr() and in interactive console.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"