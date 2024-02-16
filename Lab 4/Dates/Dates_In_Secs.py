from datetime import datetime

# Function to get datetime input from user
def get_datetime_input(prompt):
    date_str = input(prompt)
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return date

print("Enter the first date and time (YYYY-MM-DD HH:MM:SS):")
date1 = get_datetime_input(">> ")

print("Enter the second date and time (YYYY-MM-DD HH:MM:SS):")
date2 = get_datetime_input(">> ")

difference_seconds = abs((date2 - date1).total_seconds())

print("Difference between the two dates in seconds:", difference_seconds)
