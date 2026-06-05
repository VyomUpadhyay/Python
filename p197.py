import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)
    
list1[0]=900

print(list1)