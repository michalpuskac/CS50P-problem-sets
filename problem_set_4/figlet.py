"""
Implement a program that:
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""
import pyfiglet
import sys
import random

def print_usage_and_exit():
    print("Usage:")
    print("1. Output with a random font:")
    print("   python figlet.py")
    print("2. Output with a specific font:")
    print("   python figlet.py -f <font_name>")
    sys.exit(1)

def get_random_font():
    fonts = pyfiglet.Figlet().getFonts()
    return random.choice(fonts)

def main():
    # Initialize Figlet and get list of fonts
    figlet = pyfiglet.Figlet()
    fonts = figlet.getFonts()

    # Check command-line arguments
    if len(sys.argv) == 1:
        # No font specified, use a random font
        font_name = get_random_font()
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        # Font specified, validate if it exists
        font_name = sys.argv[2]
        if font_name not in fonts:
            print(f"Error: '{font_name}' is not a valid font.")
            print_usage_and_exit()
    else:
        # Incorrect usage
        print_usage_and_exit()

    # Set the chosen font
    figlet.setFont(font=font_name)

    # Prompt user for input and display output
    user_input = input("Input: ")
    print("Output:\n" + figlet.renderText(user_input))

if __name__ == "__main__":
    main()