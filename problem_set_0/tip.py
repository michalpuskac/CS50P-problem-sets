"""dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.

percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit),
remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
"""

def main():
    """Prompt the user for meal cost and tip percentage, then calculate and display the tip amount."""
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollar_str):
    """Convert a dollar amount string with a leading '$' to a float."""
    return float(dollar_str.replace("$", ""))

def percent_to_float(percent_str):
    """Convert a percentage string with a trailing '%' to a float in decimal form."""
    return float(percent_str.replace("%", "")) / 100

if __name__ == "__main__":
    main()