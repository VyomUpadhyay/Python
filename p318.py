f1=open("abc.txt","r")
f2=open("hi.txt","w")
list1=["a","e","i","o","u"]

while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch in list1:
        pass
    else:

        f2.write(ch)
f1.close()
f2.close()
print("Copied")