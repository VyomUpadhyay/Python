import random

list1=[]
for i in range(1,12):
    y=random.randint(1,20)
    list1.append(y)
    
X=int(input("Enter position =>"))
Y=int(input("Enter value =>"))

list1.insert(X,Y)

print(list1)