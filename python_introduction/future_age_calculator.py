# Ask the user for their current age
current_age = input("How old are you? ")  

# input() returns a string, so convert it to an integer
current_age = int(current_age)

# Calculate age in 2050
years_until_2050 = 2050 - 2023  # that’s 27 years
future_age = current_age + years_until_2050

# Print the result
print("In 2050, you will be", future_age, "years old.")
