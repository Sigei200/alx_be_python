# shopping_list_manager.py

def display_menu():
    """Displays the main menu options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Handles user interaction and manages the shopping_list.
    """
    shopping_list = [] # Initialize an empty shopping list

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip() # Use .strip() to remove leading/trailing whitespace

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Remove an item
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue # Go back to the menu
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Enumerate for numbered list
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break # Exit the while loop
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()