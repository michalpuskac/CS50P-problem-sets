"""In a file called bank.py, implement a program that prompts the user for a greeting. 
If the greeting starts with “hello”, output $0. 
If the greeting starts with an “h” (but not “hello”), output $20. 
Otherwise, output $100. 
Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
"""

# Define a function to process the greeting and return the appropriate dollar amount
def process(greeting):
    greeting = greeting.lower() #added for tests.. 
    # Check if the greeting starts with "hello"
    if greeting.startswith("hello"):
        return 0
    # Check if the greeting starts with "h" but is not "hello"
    elif greeting.startswith("h"):
        return 20
    # Default case for greetings not starting with "h"
    else:
        return 100


# Define the main function to encapsulate the program logic
def main():    
    # Prompt the user for a greeting, making it lowercase and removing extra spaces
    greeting = input("Greeting: ").lower().strip()
    result = process(greeting)
    print(f"${result}") 

if __name__ == "__main__":
    main()