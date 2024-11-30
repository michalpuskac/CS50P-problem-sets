"""
In a file called fuel.py, implement a program that prompts the user for a fraction,formatted as X/Y,
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.

If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

def get_fraction():
    """Prompt user to input a fraction until format of it, is X/Y.Can't divide by 0. Both has to be more than 0 or have x<y."""
    while True:
        try:
            fraction_str = input("Fraction (X/Y): ")
            x, y = map(int,fraction_str.split("/"))

            if y == 0:
                raise ValueError("Cannot divide by 0.")
            if x < 0 or y < 0 or x>y:
                raise ValueError("Invalid fraction. Make X>0 and Y>0 and X<Y")
            return x , y

        except(ValueError, ZeroDivisionError) as e :
            print (f"Error {e} Enter valid fraction, remeber can't devide by 0")

def calculate_percentage(x, y):
    """Calculte percetentage from user fraction input"""
    percentage = (x / y) *100
    return round(percentage)

def main():
    while True:
        try:
            x, y = get_fraction()
            percentage = calculate_percentage(x, y)

            if percentage <=0:
                print("E")
            elif percentage >=100:
                print("F")
            else:
                print(f"{percentage}%")

            break

        except Exception as e:
             print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
