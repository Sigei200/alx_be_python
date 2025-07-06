#!/usr/bin/env python3
"""
bank_account.py: Defines the BankAccount class for banking operations.
"""

class BankAccount:
    """
    A simple bank account class to demonstrate OOP principles.
    Encapsulates account balance and provides methods for deposit,
    withdrawal, and balance display.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float): The starting balance for the account.
                                    Defaults to 0.
        """
        # Ensure initial balance is non-negative
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__account_balance = initial_balance # Using __ for "private" convention

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__account_balance += amount
        # No return needed as per prompt, just modifies state

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.
        Returns:
            bool: True if withdrawal is successful, False otherwise.
        Raises:
            ValueError: If the withdrawal amount is not positive.
            TypeError: If the withdrawal amount is not a number.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

    # Optional: A getter for the balance, useful for testing, though not explicitly required by prompt
    # def get_balance(self):
    #     return self.__account_balance