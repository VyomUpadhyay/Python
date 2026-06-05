print("Press 1 for addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Divition")

option = int(input("Enter the option => "))
Number1 = float(input("Enter the value of the first number: "))
Number2 = float(input("Enter the value of the second number: "))

if option==1:
    print(Number1+Number2)
elif option==2:
    print(Number1-Number2)
elif option==3:
    print(Number1*Number2)
elif option==4:
    print(Number1/Number2)
else:
    print("Enter the valid option")