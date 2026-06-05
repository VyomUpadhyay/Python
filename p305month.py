import time
current = time.localtime(time.time())
d=current.tm_mday
m=current.tm_mon
y=current.tm_year

if y%4==0:
    print("The year is a leap year")
    