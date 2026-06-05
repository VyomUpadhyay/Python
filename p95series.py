number = int(input("Enter the limit => "))
subtraction = 0
Sumodd = 0
Result = Sumodd - subtraction
for i in range(1,number + 1):
    if i%2 == 0:
        print(i, end=" - ")
        subtraction = subtraction - i
    else:
        print( i , end=" + ")
        Sumodd = Sumodd + i
print("\nSum = ", Result)