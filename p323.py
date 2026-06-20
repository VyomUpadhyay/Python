f1=open("abc.txt","r")
f2=open("vowel.txt","w")
f3=open("notvowel.txt","w")
list1=["a","e","i","o","u"]

while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch in list1:
        f2.write(ch)
    elif ch not in list1:
        f3.write(ch)
f1.close()
f2.close()
f3.close()
print("Copied")
print("Copied")
print("Copied")