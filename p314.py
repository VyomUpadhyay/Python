f1=open("abc.txt","r")

while True:
    ch=f1.read(1)
    if not ch:
        break
    print(ch)

f1.close()


