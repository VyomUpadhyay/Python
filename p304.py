import time
current = time.localtime(time.time())
print("Weekday:", current.tm_wday)
print("Yearday:", current.tm_yday)
print("Hour:", current.tm_hour)
print("Minutes:", current.tm_min)
print("Seconds:", current.tm_sec)
