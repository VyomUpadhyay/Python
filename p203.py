import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)
    
count = len(list1)

print("The count of the elements is ", count)