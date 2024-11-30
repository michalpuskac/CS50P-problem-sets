"""Implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time,
a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes),
convert should return 7.5 (i.e., 7.5 hours).
"""

def convert(time):
    """Time in string format conversion to float format => '7:30' == 7.5 """
    #Split the time to hour
    hours, minutes = time.split(":")

    #Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    #Convert the time to a float
    return hours + (minutes /60)


def main():
    #Promp user for input
    user_time = input("What time is it ? ")
    
    # Validate input format and process if valid
    if ":" not in user_time:
        print("Invalid time format.")
        return

    try:
        # Convert input time to hours in float
        hours = convert(user_time)

        # Determine and print the meal time based on the time range
        if 7.0 <= hours <= 8.0:
            print("Breakfast time")
        elif 12.0 <= hours <= 13.0:
            print("Lunch time")
        elif 18.0 <= hours <= 19.0:
            print("Dinner time")
    except ValueError:
        print("Invalid time format. Please enter time in 24-hour format as #:## or ##:##.")


if __name__ == "__main__":
    main()