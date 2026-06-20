from datetime import datetime

current_time = datetime.now()

hour = current_time.hour
minute = current_time.minute
second = current_time.second

if hour >= 12:
    period = "PM"
else:
    period = "AM"

if hour == 0:
    hour_12 = 12
elif hour > 12:
    hour_12 = hour - 12
else:
    hour_12 = hour

formatted_time = f"{hour_12:02}:{minute:02}:{second:02} {period}"

print("Current time in 12-hour format:", formatted_time)
