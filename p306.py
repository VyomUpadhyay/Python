import time
current = time.localtime(time.time())
h=current.tm_hour
m=current.tm_min
s=current.tm_sec
print(h,":",m,":",s)

if h<=12:
    print("Good Morning")
elif h<=16:
    print("Good Afternoon")
else:
    print("Good Evening")
