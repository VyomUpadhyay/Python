import random
countcorrect=0
countincorrect=0
for i in range(1,6):
    
    number=random.randint(1,50)
    number1=random.randint(1,50)
    
    print("Number 1 = ", number ," Number 2 = ", number1)

    x=int(input("Enter the addition of these two numbers -> "))
    if x==(number+number1):
        countcorrect+=1
    else:
        countincorrect+=1

print("The number of correct answer is -> ", countcorrect)
print("The number of incorrect answer is -> ", countincorrect)