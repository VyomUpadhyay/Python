print("Press 1 to find the minimum and the maximun of the 2 numbers")
print("Press 2 to find the minimum and the maximun of the 3 numbers")

option = int(input("Enter the option => "))

if option==1:
    number1= float(input("Enter the first number: "))
    number2= float(input("Enter the second number: "))
    
    if number1>number2:
        print("Number 1 is greater")
    else: 
        print("Number 2 is greater")  
    
elif option==2:
    Number1= float(input("Enter the first number: "))
    Number2= float(input("Enter the second number: "))
    Number3= float(input("Enter the third number: "))
    
    if Number1>Number2 :
        if Number1>Number3:
            print("Number 1 is greater")
    
    elif Number2>Number3:
        print("Number 2 is Greater")
    
    else:
        print("Number 3 is Greater")
else: 
    print("Please select the correct option")