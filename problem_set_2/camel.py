"""Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case."""

def camel_to_snake(name):
    """Convert a camelCase string to snake_case."""
    snake_case = ""
    for char in name:
        if char.isupper():
            # Add an underscore before the lowercase character
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

def main():
    """Prompt user for a camelCase variable name and output it in snake_case."""
    camel_case_name = input("camelCase: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print("snake_case:", snake_case_name)

if __name__ == "__main__":
    main()