"""Implement a program that prompts the user for items, one per line, 
until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
Treat the user’s input case-insensitively."""


def main():
    print(f"Enter Groceries amd for exit, type 'quit'.")
    grocery_list = {}
    while True:
        try:
            item = input("").strip().lower()
            if item == "quit":
                print("\nGrocery List:")
                break

            if item in grocery_list:
                grocery_list[item] +=1
            else:
                grocery_list[item] =1

        except EOFError:
            print("\nGrocery List:")

            break

    # Sort the grocery list and display in uppercase with count
    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item.upper()}")


if __name__ == "__main__":
    main()