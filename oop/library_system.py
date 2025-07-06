#!/usr/bin/env python3
"""
library_system.py:
Demonstrates inheritance (Book, EBook, PrintBook) and composition (Library).
Models a library system with different types of books.
"""

class Book:
    """
    Base class representing a generic book with a title and an author.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an EBook, inheriting from Book.
    Includes an additional attribute for file size.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes a new EBook instance.

        Args:
            title (str): The title of the EBook.
            author (str): The author of the EBook.
            file_size (int): The file size of the EBook in KB.
        """
        super().__init__(title, author) # Call the base class (Book) constructor
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook object.
        """
        # Uses attributes from both base and derived classes
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a PrintBook, inheriting from Book.
    Includes an additional attribute for page count.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a new PrintBook instance.

        Args:
            title (str): The title of the PrintBook.
            author (str): The author of the PrintBook.
            page_count (int): The number of pages in the PrintBook.
        """
        super().__init__(title, author) # Call the base class (Book) constructor
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook object.
        """
        # Uses attributes from both base and derived classes
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Represents a library that manages a collection of various book types.
    Demonstrates composition by holding Book objects.
    """
    def __init__(self):
        """Initializes a new Library instance with an empty list to store books."""
        self.books = [] # This list will hold Book, EBook, and PrintBook instances

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book (Book): An instance of Book or its derived classes.
        """
        # Optional: Add validation to ensure it's a Book instance or derived
        if isinstance(book, Book):
            self.books.append(book)
            # print(f"Added '{book.title}' to the library.") # For debugging
        else:
            print(f"Error: Cannot add non-Book object to library: {type(book)}")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        The specific __str__ method of each book type will be called.
        """
        for book in self.books:
            print(book) # This will automatically call the __str__ method of each book object