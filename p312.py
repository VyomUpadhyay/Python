from datetime import datetime

# Get the current date and time
now = datetime.now()

# Year (four digits)
year = now.strftime("%Y")
print("Year:", year)

# Month (two digits)
month = now.strftime("%m")
print("Month (numeric):", month)

# Full month name
month_name = now.strftime("%B")
print("Month (full name):", month_name)

# Day of the month (two digits)
day = now.strftime("%d")
print("Day of the month:", day)

# Weekday (short name)
weekday = now.strftime("%a")
print("Weekday (short):", weekday)

# Full weekday name
weekday_full = now.strftime("%A")
print("Weekday (full name):", weekday_full)

# Hour (24-hour format)
hour = now.strftime("%H")
print("Hour (24-hour format):", hour)

# Minute (two digits)
minute = now.strftime("%M")
print("Minute:", minute)

# Second (two digits)
second = now.strftime("%S")
print("Second:", second)

# Day of the year
day_of_year = now.strftime("%j")
print("Day of the year:", day_of_year)

# Week number of the year
week_number = now.strftime("%U")
print("Week number (Sunday as the first day of the week):", week_number)
