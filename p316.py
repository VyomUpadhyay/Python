f1=open("abc.txt","r")
f2=open("pqr.txt","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    f2.write(ch)
f1.close()
f2.close()
print("Copied")
"""
1->2 , space xopy X
1->2 , vowel X
1->2 , upper X
1->2 , space , 7
1-2 , u-l-u
1->2 upper
 =>3 lower
1->2 vowel
 -> other
"""