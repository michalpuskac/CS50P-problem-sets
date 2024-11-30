"""Implement a program that prompts the user for a date, 
anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list below.

Then output that same date in YYYY-MM-DD format. 
If the user’s input is not a valid date in either format, 
prompt the user again. Assume that every month has no more than 31 days; 
no need to validate whether a month has 28, 29, 30, or 31 days."""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date_input = input("Date (mm/dd/yy or month d,y,): ").strip()
        
        try:
            # Check for numeric format MM/DD/YYYY
            if "/" in date_input:
                month, day, year = map(int, date_input.split("/"))
            # Check for textual format Month DD, YYYY
            elif "," in date_input:
                month_name, day_year = date_input.split(" ", 1)
                day, year = day_year.split(", ")
                month = months.index(month_name) + 1
                day = int(day)
                year = int(year)
            else:
                raise ValueError("Invalid format")
            
            # Validate date values
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Invalid date")

            # Print in ISO 8601 format
            print(f"{year:04}-{month:02}-{day:02}")
            break
        
        except (ValueError, IndexError):
            print("Invalid date. Please try again.")

if __name__ == "__main__":
    main()