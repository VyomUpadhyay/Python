f1=open("abc.txt","r")
f2=open("def.txt","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.islower():
        print(f2.write(ch.lower()),end="")

    elif ch.isupper():
        print(f2.write(ch.lower()),end="")
        f2.write(ch)
f1.close()
f2.close()
print("Copied")