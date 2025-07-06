#!/usr/bin/env python3
"""
library_management.py: Implements Book and Library classes for a basic
library management system, demonstrating OOP concepts.
"""

class Book:
    """
    Represents a book in the library with a title, author,
    and checkout status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title       # Public attribute
        self.author = author     # Public attribute
        self._is_checked_out = False  # Private attribute (convention)

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True # Indicate successful checkout
        return False # Indicate it was already checked out

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True # Indicate successful return
        return False # Indicate it was already available

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    """
    Manages a collection of Book instances, providing methods for
    adding, checking out, returning, and listing books.
    """
    def __init__(self):
        """Initializes a new Library instance with an empty list of books."""
        self._books = [] # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return
        self._books.append(book)
        # print(f"'{book.title}' by {book.author} added to the library.") # For debugging

    def check_out_book(self, title):
        """
        Checks out a book by its title if it is available.

        Args:
            title (str): The title of the book to check out.
        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out(): # Call the Book's check_out method
                    # print(f"'{title}' has been checked out.") # For debugging
                    return True
                else:
                    # print(f"'{title}' is already checked out.") # For debugging
                    return False
        # print(f"'{title}' not found in the library.") # For debugging
        return False # Book not found

    def return_book(self, title):
        """
        Returns a book by its title if it was checked out.

        Args:
            title (str): The title of the book to return.
        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book(): # Call the Book's return_book method
                    # print(f"'{title}' has been returned.") # For debugging
                    return True
                else:
                    # print(f"'{title}' was not checked out.") # For debugging
                    return False
        # print(f"'{title}' not found in the library.") # For debugging
        return False # Book not found

    def list_available_books(self):
        """
        Prints the title and author of all available (not checked out) books.
        If no books are available, it prints a message.
        """
        available_found = False
        for book in self._books:
            if book.is_available(): # Call the Book's is_available method
                print(f"{book.title} by {book.author}")
                available_found = True
        if not available_found:
            # This case is not explicitly shown in expected output,
            # but good for robustness if library is empty or all books are checked out.
            # The provided example implies it should just print nothing if no books.
            pass # The sample output just shows nothing if no books match.