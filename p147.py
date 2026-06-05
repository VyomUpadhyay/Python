import random
total=0
counteven=0
countodd=0
for i in range(1,6):
    x=random.randint(1,50)
    print(x)
    total+=x
    if x%2==0:
        counteven+=1
    else:
        countodd+=1
print("The total is -> ",total)
print("The even count is -> ",counteven)
print("The odd count is -> ",countodd)