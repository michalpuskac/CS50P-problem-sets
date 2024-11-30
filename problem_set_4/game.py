import random
"""Implement a program that:
Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit."""


def get_positive_integer(prompt):
    """Prompt the user for a positive integer and return it."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    # Get difficulty level from user
    level = get_positive_integer("Enter the level of difficulty (gues to difficulty 1 or higher): ")
    
    # Generate target number within the chosen level
    target_number = random.randint(1, level)
    
    # Prompt the user to guess the number
    while True:
        guess = get_positive_integer("Guess the number: ")

        # Compare guess with target number
        if guess > target_number:
            print("Too large!")
        elif guess < target_number:
            print("Too small!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()