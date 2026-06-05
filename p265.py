import random
d1 = {}
n=int(input("Ente rlimit =>"))

for i in range(1,n+1):
    k=i
    salary=random.randint(10000,50000)
    d1[k]=salary
    
print(d1)