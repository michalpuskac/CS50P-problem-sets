"""Implement a program that expects exactly one command-line argument,
 the name (or path) of a CSV file in Pinocchio’s format,
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
Format the table using the library’s grid format.
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv,
 or if the specified file does not exist, the program should instead exit via sys.exit.
"""

import csv
import sys
import os
from tabulate import tabulate

def main():
    #Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python pizza.py <file.csv>")
        sys.exit()
    filename = sys.argv[1]

    #Check if the file exists
    if not os.path.isfile(filename):
        print(f"The file {filename} does not exist.")
        sys.exit()

    #Check if the file is a .csv file
    if not filename.endswith('.csv'):
        print(f"The file {filename} is not a .csv file.")
        sys.exit()

    #Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    #Print the data in grid format
    print(tabulate(data, tablefmt="grid"))

if __name__ == "__main__":
    main()
