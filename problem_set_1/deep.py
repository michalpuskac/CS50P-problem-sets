"""Implement a program that prompts the user for the answer to the Great Question of Life, 
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

# Define a set of valid answers, accounting for both "42" and written forms
valid_answers = {"42", "forty-two", "forty two"} #Sets are faster for membership testing than lists 

# Prompt the user to answer, making the input lowercase and removing extra spaces
user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

# Check if the input is in the set of valid answers and print the appropriate response
print("Yes" if user_input in valid_answers else "No")

