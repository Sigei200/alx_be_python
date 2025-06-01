# pattern_drawing.py

# Ask the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")  # Print * without moving to next line
    print()  # Move to the next line after each row
    row += 1  # Move to the next row
