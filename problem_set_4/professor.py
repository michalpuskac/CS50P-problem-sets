"""In a file called professor.py, implement a program that:
- Prompts the user for a level,n. If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
  digits. No need to support operations other than addition (+).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), 
  the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
  If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user 
for a level and returns 1, 2, or 3, and generate_integer
returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
"""
import random

def get_level():
    """Prompt the user for a level (1, 2, or 3) and return it."""
    while True:
        try:
            level = int(input("Level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter an integer (1, 2, or 3).")

    else:
        print ("Invalid entry")        
        return  get_level()

def generate_integer(level):
    """Generate a random integer with the specified number of digits based on level."""
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")

def ask_problem(x, y):
    """Prompt the user to solve the math problem x + y and return True if correct within 3 tries, else False."""
    tries = 0
    while tries < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return True
            else:
                print("EEE")
                tries += 1
        except ValueError:
            print("EEE")
            tries += 1

    # After 3 failed attempts, show the correct answer
    print(f"The correct answer is {x + y}")
    return False


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        if ask_problem(x, y):
            score += 1
    print(f"Score: {score}/10")

if __name__ == "__main__":
    main()