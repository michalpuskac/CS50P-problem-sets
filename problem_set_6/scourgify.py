"""
Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
"""

import csv
import sys
import os

def main():
    # Check for exactly two command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py <input.csv> <output.csv>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check if the input file exists and is a CSV file
    if not os.path.isfile(input_filename):
        print(f"The file {input_filename} does not exist.")
        sys.exit(1)
    if not input_filename.endswith(".csv"):
        print(f"The file {input_filename} is not a .csv file.")
        sys.exit(1)

    # Read the input CSV and write to the output CSV with the correct format
    try:
        with open(input_filename, "r") as input_file:
            reader = csv.DictReader(input_file)
            with open(output_filename, "w", newline="") as output_file:
                # Define field names for the output file
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()
                
                # Process each row in the input file
                for row in reader:
                    # Split the name into first and last
                    last, first = row["name"].split(", ")
                    # Write the row to the output file
                    writer.writerow({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        print(f"Could not read {input_filename}")
        sys.exit(1)

if __name__ == "__main__":
    main()