"""
Implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user is owed. Assume that the user will only input integers,
and ignore any integer that isn’t an accepted denomination.

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents 
and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
"""

def main():
    #Set cost of the item
    cost = 50
    amount_due = cost

    #Accepted coin denominations
    accepted_coins = [25, 10, 5]

    #Continue prompting until amount due is covered
    while amount_due >0:
        try:
            print(f"Amoount Due: {amount_due}.cents")
            #Promt user to insert a coin
            coin = int(input("Insert Coin: "))

            #Check if inserted coin is in accepted denominations
            if coin in accepted_coins:
                amount_due -= coin
            else:
                print("\nInvalid coin denomination. Please insert 5, 10, or 25 cents.")
        except ValueError:
            print("\nPlease insert a valid integer")

    #Calculate and print the change owed, if any 
    changed_owed = abs(amount_due)
    print(f"\nChange Owed: {changed_owed} cents.")

if __name__ == "__main__":
    main()