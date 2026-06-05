print("Press 1 to Pizza")
print("Press 2 to Dosa")
print("Press 3 to Punjabi")
print("Press 4 to Chinese")
print("Press 5 to Mexican")

option = int(input("Enter the option value: "))

if option==1:
    Quantity = int(input("Enter the quantity of the pizza: "))
    print("The total bill of pizza is = ", Quantity*300)
elif option==2:
    Quantity = int(input("Enter the quantity of the Dosa: "))
    print("The total bill of Dosa is = ", Quantity*200)
elif option==3:
    Quantity = int(input("Enter the quantity of the Punjabi food: "))
    print("The total bill od Punjabi food is = ", Quantity*225)
elif option==4:
    Quantity = int(input("Enter the quantity of the Chinese food: "))
    print("The total bill of Chinese food is = ", Quantity*250)
elif option==5:
    Quantity = int(input("Enter the quantity of the Mexican food: "))
    print("The total bill of Mexican food is = ", Quantity*220)
else:
    print("Enter the valid option")
