shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            user_input = str(input("Enter the item you wish to add: "))
            adding = shopping_list.append(user_input)
            print(f"your list {shopping_list}")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            user_input = str(input("Enter the item you wish to remove: "))
            if user_input in shopping_list:
                removing = shopping_list.remove(user_input)
            else:
                print(f"{user_input}was not found in the shopping list.")
            print(f"your list {shopping_list}")
            pass
        elif choice == '3':
            # Display the shopping list
            print(f"your list {shopping_list}")
            pass
        elif choice == '4':
            print(f"Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

display_menu()