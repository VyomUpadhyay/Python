Limit = int(input("Enter the limit of the number => "))
countdivisibleby3 = 0
countdivisibleby7 = 0
sum3 = 0
sum7 = 0

for i in range(1,Limit+1):
    if i%3==0:
        countdivisibleby3 = countdivisibleby3 + 1
        sum3 = sum3 + i
    elif i%7==0:
        countdivisibleby7 = countdivisibleby7 + 1
        sum7 = sum7 + i
print("The count of the numbers which are divisible by 3 is ", countdivisibleby3)
print("The sum of the numbers which are divisible by 3 is ", sum3)
print("The count of the numbers which are divisible by 7 is ", countdivisibleby7)
print("The sum of the numbers which are divisible by 7 is ", sum7)

