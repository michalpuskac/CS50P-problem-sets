"""Implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 
 names with 
 commas and one and, as in the below:"""

import inflect
import sys

# Initialize the inflect engine
p = inflect.engine()

def main():
    names = []

    # Prompt the user for names until Control-D (EOFError)
    print("Enter names, one per line (press Control-D when done):")
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    # Generate the output
    if names:
        # Join names with commas and "and" in the correct format
        farewell = p.join(names)
        print(f"Adieu, adieu, to {farewell}")

if __name__ == "__main__":
    main()