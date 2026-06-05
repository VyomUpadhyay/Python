import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)
    
list2=[]
for i in range(1,12):
    x=random.randint(1,20)
    list1.append(x)
    
print(list1)
print(list2)

list1.extend(list2)
print(list1)
