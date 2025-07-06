#!/usr/bin/env python3
"""
explore_datetime.py:
A script to demonstrate usage of Python's datetime module.
It displays the current date/time and calculates a future date.
"""

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and prints the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.now() # Get the current date and time
    # Format the datetime object into a string
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")
    return current_date # Return the datetime object for further use if needed

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and prints it in "YYYY-MM-DD" format.
    """
    while True:
        try:
            # Prompt user for input and convert it to an integer
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            num_of_days = int(days_to_add_str)
            if num_of_days < 0:
                print("Please enter a non-negative number of days.")
                continue
            break # Exit loop if input is valid
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a whole number.")

    # Get the current date (without time for easier future date calculation based on current day)
    # Or, we can use the current_date from display_current_datetime for consistency
    # Let's use datetime.now() again to be independent, but we could also pass it from display_current_datetime
    current_datetime_for_future = datetime.now()

    # Calculate the future date using timedelta
    future_date = current_datetime_for_future + timedelta(days=num_of_days)

    # Format the future date to "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


if __name__ == "__main__":
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    calculate_future_date()