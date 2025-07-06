#!/usr/bin/env python3
"""
main-0.py: Interfaces with the BankAccount class using command line arguments.
Performs deposit, withdraw, or display balance operations.
"""

import sys
# Import the BankAccount class from the bank_account module
# Ensure bank_account.py is in the same directory or on Python's path
from bank_account import BankAccount

def main():
    """
    Main function to parse command line arguments and interact with BankAccount.
    """
    # Create a BankAccount instance with an example starting balance
    # For testing purposes, you can adjust this initial balance.
    account = BankAccount(100.0) # Using float for consistency

    # Check if enough arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1) # Exit with an error code

    # Parse the command and optional amount from the first argument
    # Example: "deposit:50" -> command="deposit", params=["50"]
    # Example: "display"    -> command="display", params=[]
    parts = sys.argv[1].split(':')
    command = parts[0]
    params = parts[1:] # This will be an empty list if no ':' is present

    amount = None
    if params: # Check if params list is not empty
        try:
            amount = float(params[0])
        except ValueError:
            print(f"Error: Amount '{params[0]}' must be a valid number.")
            sys.exit(1)

    # Perform the requested operation
    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except (ValueError, TypeError) as e:
            print(f"Error depositing: {e}")
            sys.exit(1)
    elif command == "withdraw" and amount is not None:
        try:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except (ValueError, TypeError) as e:
            print(f"Error withdrawing: {e}")
            sys.exit(1)
    elif command == "display":
        # The display command does not take an amount
        if amount is not None:
             print("Warning: 'display' command does not require an amount. Ignoring provided amount.")
        account.display_balance()
    else:
        print("Invalid command or missing amount for deposit/withdraw.")
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

if __name__ == "__main__":
    main()