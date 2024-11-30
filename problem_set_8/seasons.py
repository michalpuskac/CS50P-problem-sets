"""Implement a program that prompts the user for their date of birth in YYYY-MM-DD format 
and then sings prints how old they are in minutes, rounded to the nearest integer,
using English words instead of numerals, just like the song from Rent,
without any and between words. Since a user might not know the time at which they were born,
assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date.
And assume that the current time is also midnight.
In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date.
Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

Exit via sys.exit if the user does not input a date in YYYY-MM-DD format.
Ensure that your program will not raise any exceptions.
Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py,
one or more functions that test your implementation of any functions besides main in seasons.py thoroughly,
each of whose names should begin with test_ so that you can execute your tests.
"""

from datetime import date
import inflect
import sys


# YYYY-MM-DD
def get_birth_date():
    try:
        birth_date = input("Date of birth YYYY-MM-DD: ")
        year,month,day = map(int,birth_date.split("-"))
        return date(year, month, day)
    except (ValueError, TypeError):
        sys.exit("Invalid date format. Please use YYYY-MM-DD format.")



def calculate_minutes_lived(birth_date, today=None):
    # Use today's date if not provided (default to date.today())
    if today is None:
        today = date.today()
    days_lived = (today - birth_date).days
    return days_lived * 24 * 60


def convert_to_words(number):
    p = inflect.engine()
    return  p.number_to_words(number, andword= "").replace(",","")



def main():
    birth_date =  get_birth_date()
    minutes_lived = calculate_minutes_lived(birth_date)
    words = convert_to_words(minutes_lived)
    print(f"{words} minutes.")


if __name__ == "__main__":
    main()