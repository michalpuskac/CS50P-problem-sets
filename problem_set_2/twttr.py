"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
much like Twitter was originally called twttr. In a file called twttr.py,
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase."""

def shorten(user_input):
    """Remove all vowels from the input string."""
    #vowels = "AEIOUaeiou"
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'} #Sets provide faster lookup times for membership checks (in), making it more efficient for filtering out characters, especially if the input text is long.
    result = "".join(char for char in user_input if char not in vowels) 
    return result


def main():
    user_input = input("Input: ")
    print("Output:", shorten(user_input))

if __name__ == "__main__":
    main()
