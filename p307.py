import time
current = time.localtime(time.time())
h=current.tm_hour
m=current.tm_min
s=current.tm_sec
print(h,":",m,":",s)

if h<12:
    print(h,":",m,":",s, "a.m")
else:
    print(h,":",m,":",s, "p.m")
