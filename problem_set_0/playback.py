#Implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

user_input = input("Write something with spaces: ")
print(f"Read with a slower pace: {user_input.replace(' ', '...')}")