#!/usr/bin/env python3
"""
main.py:
Command-line interface for the robust division calculator.
Takes two arguments (numerator and denominator) and prints the result
from the safe_divide function.
"""

import sys
# Import the safe_divide function from the robust_division_calculator module
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command-line arguments for division.
    """
    # Check if the correct number of arguments are provided (script name + 2 arguments)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1) # Exit with an error code, indicating incorrect usage

    # sys.argv[0] is the script name itself
    # sys.argv[1] is the first argument (numerator)
    # sys.argv[2] is the second argument (denominator)
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function with the command-line arguments
    result = safe_divide(numerator, denominator)

    # Print the result returned by safe_divide
    print(result)

if __name__ == "__main__":
    main()