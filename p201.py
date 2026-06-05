import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)
    
a=list1[2:7:2] 
print(a)
b=list1[::3]
print(b)
c=list1[0:8:2]
print(c)