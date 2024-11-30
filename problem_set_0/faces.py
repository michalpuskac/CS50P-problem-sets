""" Implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). 
All other text should be returned unchanged.
Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. 
You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file."""

def main():
    """Prompts the user for input, converts emoticons, and prints the result."""
    input_text = input("Enter text with emoticons :) or :( : ")
    converted_text = convert(input_text)
    print(converted_text)

def convert(input_str):
    """Replaces :) with 🙂 and :( with 🙁 in the given string."""
    input_str = input_str.replace(":)", "🙂")
    input_str = input_str.replace(":(", "🙁")
    return input_str

    #alternative simpler way: return input_str.replace(":)", "🙂").replace(":(", "🙁")
    
if __name__ == "__main__":
    main()