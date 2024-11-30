"""
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements
or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.

"""

def is_valid(s):
    return (
        start_with_letter(s) 
        and has_valid_length(s) 
        and has_no_punctuation(s) 
        and has_valid_numbers(s)
    )


def start_with_letter(s):
    """All vanity plates must start with at least two letters"""
    return len(s) >= 2 and s[:2].isalpha()


def has_valid_length(s):
    """Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters."""
    return 2 <= len(s) <= 6


def has_valid_numbers(s):
    """Numbers cannot be used in the middle of a plate; they must come at the end.
    For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
    The first number used cannot be a ‘0’."""
    # Check if there are any digits in the stringAA
    found_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and not found_digit:  # First digit cannot be '0'
                return False
            found_digit = True
        elif found_digit:
            # If we've seen a digit, all subsequent characters must be digits
            return False
    return True


def has_no_punctuation(s):
    """No periods, spaces, or punctuation marks are allowed"""
    return all(char.isalnum() for char in s)


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()