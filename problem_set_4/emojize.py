"""Implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, 
converting any codes (or aliases) therein to their corresponding emoji.

See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.
"""

import emoji
user_input = input("Input: ")
print(emoji.emojize(f"Output: {user_input}"))