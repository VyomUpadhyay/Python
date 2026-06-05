import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)
    
for x in list1:
    if x%2==1:
        print(x)