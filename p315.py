f1=open("abc.txt","r")
f2=open("pqr.txt","w")
while True:
    ch=f1.read(1)
    if not ch:
        break

f1.close()