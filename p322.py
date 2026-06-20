f1=open("abc.txt","r")
f2=open("upper.txt","w")
f3=open("lower.txt","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.upper():
        f2.write(ch.upper())
    elif ch.lower():
        f3.write(ch.lower())
    else:
        pass
f1.close()
f2.close()
f3.close()
print("Copied")
print("Copied")