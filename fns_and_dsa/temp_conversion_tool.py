#!/usr/bin/env python3
"""
temp_conversion_tool.py:
A script for converting temperatures between Celsius and Fahrenheit.
Demonstrates the use of global variables for conversion factors.
"""

# Define Global Conversion Factors
# Note: Using float literals to ensure float division
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR.

    Args:
        fahrenheit (float or int): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # (F - 32) * (5/9)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR.

    Args:
        celsius (float or int): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # (C * 9/5) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction for temperature conversion.
    Prompts for temperature and unit, performs conversion, and displays result.
    """
    while True: # Loop to allow retrying on invalid input
        try:
            temp_str = input("Enter the temperature to convert: ")
            # Attempt to convert input to a float. If this fails, ValueError is raised.
            temperature = float(temp_str)
            break # Exit loop if conversion is successful
        except ValueError:
            # Raise a specific error message if input is not numeric
            print("Invalid temperature. Please enter a numeric value.")
            continue # Go back to the beginning of the loop

    while True: # Loop to ensure valid unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break # Exit loop if unit is valid
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # Perform conversion based on the unit
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")

if __name__ == "__main__":
    main()