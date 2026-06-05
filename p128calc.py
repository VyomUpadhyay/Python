def caclculator():
    print("Press 1 for addtion")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")

    option = str(input("Enter the option => "))
    if option==1:
        number1= int(input("Enter number 1: "))
        number2= int(input("Enter number 2: "))
        print("The addtion of the two numbers is = ",number1+number2 )
    elif option==2:
        number1= int(input("Enter number 1: "))
        number2= int(input("Enter number 2: "))
        print("The subtraction of the two numbers is = ",number1-number2 )
    elif option==3:
        number1= int(input("Enter number 1: "))
        number2= int(input("Enter number 2: "))
        print("The multiplication of the two numbers is = ",number1*number2 )
    elif option==4:
        number1= int(input("Enter number 1: "))
        number2= int(input("Enter number 2: "))
        print("The division of the two numbers is = ",number1/number2 )
    else:
        print("Enter the correct option")

def add():
    number1= int(input("Enter number 1: "))
    number2= int(input("Enter number 2: "))
    print("The addtion of the two numbers is = ",number1+number2 )

def sub():
    number1= int(input("Enter number 1: "))
    number2= int(input("Enter number 2: "))
    print("The subtraction of the two numbers is = ",number1-number2 )
    
def mul():
        number1= int(input("Enter number 1: "))
        number2= int(input("Enter number 2: "))
        print("The multiplication of the two numbers is = ",number1*number2 )
def div():
    number1= int(input("Enter number 1: "))
    number2= int(input("Enter number 2: "))
    print("The division of the two numbers is = ",number1/number2 )


caclculator()