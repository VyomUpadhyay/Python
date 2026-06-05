import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)
    
print(list1[0:5])
print(list1[:9])
print(list1[5:])
print(list1[2:5])
print(list1[2:9])
print(list1[1:8:2])
print(list1[1:8:3])