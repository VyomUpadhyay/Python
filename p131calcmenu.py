def add():
    number1 = int(input("Enter the number 1-> "))
    number2 = int(input("Enter the number 2-> "))
    print("The addtion of the two numbers is ",number1+number2)
def sub():
    number1 = int(input("Enter the number 1-> "))
    number2 = int(input("Enter the number 2-> "))
    print("The subtraction of the two numbers is ",number1-number2)
def mul():
    number1 = int(input("Enter the number 1-> "))
    number2 = int(input("Enter the number 2-> "))
    print("The multiplication of the two numbers is ",number1*number2)
def div():
    number1 = int(input("Enter the number 1-> "))
    number2 = int(input("Enter the number 2-> "))
    print("The division of the two numbers is ",number1/number2)

print("Press 1 to perform addtion")
print("Press 2 to perform subtaction")
print("Press 3 to perform multiplication")
print("Press 4 to perform division")
option = int(input("Enter the option value -> "))

if option==1:
    add()
elif option==2:
    sub()
elif option==3:
    mul()
elif option==4:
    div()
else:
    print("Enter the correct option")