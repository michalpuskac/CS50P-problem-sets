"""Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
"""

def get_user_input():
    """Prompt the user for an arithmetic expression and return the input as a string."""
    user_input = input("Expression: ")
    return user_input

def valid_operator(y):
    """Check if the given operator is one of the valid arithmetic operators."""
    return y in {"+", "-", "*", "/"}

def valid_expression(expression):
    """Validate that the given expression is in the correct format and contains valid integers and operator."""
    x, y, z = expression.split()

    if not x.isdigit() or not z.isdigit():
        return False

    x, z = int(x), int(z)

    if valid_operator(y):
        if y == "/" and z == 0:
            return False  # Division by zero is not allowed
        return True
    else:
        return False

def calculate_result(expression):
    """Calculate the result of a valid arithmetic expression."""
    x, y, z = expression.split()
    x, z = int(x), int(z)

    # Calculate based on the operator and check for division by zero    
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z 
    elif y == "/":
        return x / z


def main():
    user_expression = get_user_input()

    if valid_expression(user_expression):
        result = calculate_result(user_expression)

        # Format the result to one decimal place
        formatted_result = format(result, ".1f")    
        print(f"{formatted_result}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
