f1=open("abc.txt","r")
f2=open("def.txt","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch==" ":
        ch = ""
    f2.write(ch)
f1.close()
f2.close()
print("Copied")