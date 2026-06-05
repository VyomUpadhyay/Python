import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)

X=int(input("Enter value 1 => "))
Y=int(input("Enter value 2 => "))

list1.append(X)
list1.append(Y)

print(list1)
