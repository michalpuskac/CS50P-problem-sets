"""Implement a program that expects exactly one command-line argument,
 the name (or path) of a Python file, and outputs the number of lines of code in that file,
 excluding comments and blank lines. 
If the user does not specify exactly one command-line argument,
 or if the specified file’s name does not end in .py,
 or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. 
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank."""

import sys 
import os 

def count_lines_of_code(filename):
    try:
        with open (filename, "r") as file:
            lines = file.readlines()
            code_lines = 0

            for line in lines:
                line =line.rstrip()
                if not line:
                    continue
                if line.startswith("#") and not line.lstripstartswith('"""'):
                    continue
                code_lines += 1
            return code_lines

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        print("Usage: python lines.py <filename.py>")
        sys.exit(1)

    filename = sys.argv[1]
    total_lines = count_lines_of_code(filename)
    print(f"Total lines of code (excluding comments and blanks) in '{filename}': {total_lines}")