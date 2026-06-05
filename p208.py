import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)
    
list2=[]
for i in range(1,12):
    x=random.randint(1,20)
    list1.append(x)
    
list2.extend(list1)

print("The list after combining is ")
print(list2)