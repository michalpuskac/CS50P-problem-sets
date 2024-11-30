'''Implement a program that enables a user to place an order, prompting them for items, one per line,
 until the user inputs control-d (which is a common way of ending one’s input to a program).
After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
Treat the user’s input case insensitively.
Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.'''

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

"""
prompt user to place order 
one per line
until control-d input

after each item show total Cost prefixed with $ formatted on two decimal

input -> caseintesivly
ignore input which are not item
assume every item on menu is titlecased
"""


def display_menu():
    print("Menu:")
    print("-" * 20)
    for item, price in menu.items():
        print(f"{item:<20} ${price:.2f}")  # Left-aligns item, formats price with 2 decimals
    print("-" * 20)


def main ():
    display_menu()
    print(f"For end of order type quit.")

    total_cost = 0
    while True:
        try:
            item = input("Item: ").title()

            if item == "Quit":
                print("\nOrder complete.")
                break

            if item in menu:
                total_cost += menu[item]
                print(f"Total Cost:$ {total_cost:.2f}")
            else:
                print("Item not on menu, please try again.")
        except EOFError:  # Detect control-d
            print("\nOrder complete.")
            break

if __name__ == "__main__":
    main()