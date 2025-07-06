#!/usr/bin/env python3
"""
shopping_list_manager.py:
A simple command-line application to manage a shopping list.
Allows adding, removing, and viewing items in a list.
"""

def display_menu():
    """Prints the main menu options to the console."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager application.
    Initializes the shopping list and handles user interactions.
    """
    shopping_list = [] # Initialize an empty list to store shopping items

    while True:
        display_menu() # Show the menu to the user
        choice = input("Enter your choice: ") # Get user input

        if choice == '1':
            # Add Item functionality
            item = input("Enter the item to add: ")
            shopping_list.append(item) # Add the item to the list
            print(f"'{item}' added to the list.")
        elif choice == '2':
            # Remove Item functionality
            if not shopping_list: # Check if the list is empty first
                print("Your shopping list is empty. Nothing to remove.")
                continue # Go back to the beginning of the loop

            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove) # Remove the first occurrence of the item
                print(f"'{item_to_remove}' removed from the list.")
            else:
                print(f"'{item_to_remove}' not found in the list.")
        elif choice == '3':
            # View List functionality
            if not shopping_list: # Check if the list is empty
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Enumerate for numbered list
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            # Exit functionality
            print("Goodbye!")
            break # Exit the while loop
        else:
            # Invalid choice handling
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()