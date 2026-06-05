Number = int(input("Enter the limit to check the odd and even number till it => "))
Counteven = 0
Countodd = 0
Sumeven = 0
Sumodd = 0

for i in range(1, Number):
    if i%2==0:
        print(i, "is even")
        Counteven = Counteven + 1
        Sumeven = Sumeven + i
    else:
        print(i, "is odd")
        Countodd = Countodd + 1
        Sumodd = Sumodd + i
        
print("Sum of Even numbers is =",Sumeven, "Count of even numbers is =",Counteven)
print("Sum of odd numbers is =",Sumodd, "Count of odd numbers is =",Countodd)