Number = int(input("Enter the limit => "))
Sumeven = 0
Sumodd = 0
Result = 0   

for i in range(1,Number+1):
    if Number%2==0:
        print(i*i, end=" ")
        Sumeven = Sumeven + i*i
    else:
        print(i*i*i, end=" + ")
        Sumodd = Sumodd + i*i*i
Result= Sumeven+Sumodd

print("\nSum = ", Result)