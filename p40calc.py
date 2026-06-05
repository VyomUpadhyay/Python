print("Press + for addition")
print("Press - for Subtraction")
print("Press * for Multiplication")
print("Press / for Divition")

option = str(input("Enter the option => "))
Number1 = float(input("Enter the value of the first number: "))
Number2 = float(input("Enter the value of the second number: "))

if option== '+':
    print(Number1+Number2)
elif option=='-':
    print(Number1-Number2)
elif option=='*':
    print(Number1*Number2)
elif option=='/':
    print(Number1/Number2)
else:
    print("Enter the valid option")