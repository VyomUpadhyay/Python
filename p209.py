import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)
    
list2=[]
for i in range(1,12):
    x=random.randint(1,20)
    list1.append(x)
    
for x in list1:
    if x in list2:
        print(x)