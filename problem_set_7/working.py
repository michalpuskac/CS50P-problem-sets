"""
Implement a function called convert that expects a str in any of the 12-hour formats 
below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). 
Expect that AM and PM will be capitalized (with no periods therein) 
and that there will be a space before each. Assume that these times are representative of actual times,
not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
"""

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
        s (str): A 12-hour time string in one of the following formats:
            - "9:00 AM to 5:00 PM"
            - "9 AM to 5 PM"
            - "9:00 AM to 5 PM"
            - "9 AM to 5:00 PM"
    Returns:
        str: The corresponding 24-hour time string (e.g., "09:00 to 17:00").
    """
    # Define a regular expression pattern to match the expected 12-hour time formats
    pattern = r'^(\d{1,2}):?(\d{2})?\s*(AM|PM)\sto\s(\d{1,2}):?(\d{2})?\s*(AM|PM)$'

    # Use the re.search() function to find a match in the input string
    match = re.search(pattern, s)

    if match:
        # Extract the hour, minute, and AM/PM values from the match groups
        start_hour = int(match.group(1))
        start_minute = int(match.group(2)) if match.group(2) else 0
        start_period = match.group(3)
        end_hour = int(match.group(4))
        end_minute = int(match.group(5)) if match.group(5) else 0
        end_period = match.group(6)

        # Validate the times
        if start_hour < 1 or start_hour > 12 or end_hour < 1 or end_hour > 12:
            raise ValueError("Invalid hour value")
        if start_minute < 0 or start_minute > 59 or end_minute < 0 or end_minute > 59:
            raise ValueError("Invalid minute value")

        # Convert the 12-hour times to 24-hour format
        if start_period == "PM" and start_hour != 12:
            start_hour += 12
        if end_period == "PM" and end_hour != 12:
            end_hour += 12
        if start_period == "AM" and start_hour == 12:
            start_hour = 0
        if end_period == "AM" and end_hour == 12:
            end_hour = 0

        # Format the output string
        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
    else:
        raise ValueError("Input string not in expected format")


if __name__ == "__main__":
    main()