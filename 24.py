import calendar

# Read input
month, day, year = map(int, input().split())

# Get the day of the week
day_of_week = calendar.day_name[calendar.weekday(year, month, day)]

# Print the day in capital letters
print(day_of_week.upper())