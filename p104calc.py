while True:
    print("Press option 1 for addition")
    print("Press option 2 for subtraction")
    print("Press option 3 for multiplicaton")
    print("Press option 4 for division")
    print("Press option 5 for exit")
    option = int(input("Enter the option => "))
    if option==1:
        Number1 = float(input("Enter the value of the first number: "))
        Number2 = float(input("Enter the value of the second number: "))
        print("The addition of the two numbers is => ", Number1+Number2)
    elif option==2:
        Number1 = float(input("Enter the value of the first number: "))
        Number2 = float(input("Enter the value of the second number: "))        
        print("The subtaction of the two numbers is => ", Number1-Number2)
    elif option==3:
        Number1 = float(input("Enter the value of the first number: "))
        Number2 = float(input("Enter the value of the second number: "))        
        print("The multiplication of the two numbers is => ", Number1*Number2)
    elif option==4:
        Number1 = float(input("Enter the value of the first number: "))
        Number2 = float(input("Enter the value of the second number: "))
        print("The division of the two numbers is => ", Number1/Number2)
    elif option==5:
        break
    else:
        print("Please enter the valid option")