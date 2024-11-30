"""Implement a function called validate that expects an IPv4 address 
as input as a str and then returns True or False, respectively, 
if that input is a valid IPv4 address or not."""

import re

def validate(ip):
    # Define the regular expression pattern for an IPv4 address
    pattern = r"^(0|[1-9][0-9]{0,2})\.(0|[1-9][0-9]{0,2})\.(0|[1-9][0-9]{0,2})\.(0|[1-9][0-9]{0,2})$"
    
    # Match the pattern against the input IP address
    match = re.match(pattern, ip)
    
    if match:
        # Extract each number in the IP address
        parts = [int(part) for part in match.groups()]
        # Check if each part is within the range 0-255
        return all(0 <= part <= 255 for part in parts)
    
    return False


def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()