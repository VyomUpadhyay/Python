while True:
    print("Press 1 to Pizza")
    print("Press 2 to Dosa")
    print("Press 3 to Punjabi")
    print("Press 4 to Chinese")
    print("Press 5 to Mexican")
    print("Press 6 to exit")

    option = int(input("Enter the option value: "))
    pizza = 0
    dosa = 0
    punjabi = 0
    chinese = 0
    mexican = 0
    Bill = 0
    TotalBill = pizza + dosa + punjabi + chinese + mexican
    if option==1:
        Quantity = int(input("Enter the quantity of the pizza: "))
        pizza = Quantity*300
        print("The total bill of pizza is = ", ((Quantity*300)))

    elif option==2:
        Quantity = int(input("Enter the quantity of the Dosa: "))
        dosa = Quantity*200
        print("The total bill of Dosa is = ", Bill+(Quantity*200))
    elif option==3:
        Quantity = int(input("Enter the quantity of the Punjabi food: "))
        punjabi = Quantity*225
        print("The total bill of Punjabi food is = ", Bill+(Quantity*225))
    elif option==4:
        Quantity = int(input("Enter the quantity of the Chinese food: "))
        chinese = Quantity*250
        print("The total bill of Chinese food is = ", Bill+(Quantity*250))
    elif option==5:
        Quantity = int(input("Enter the quantity of the Mexican food: "))
        mexican = Quantity*220
        print("The total bill of Mexican food is = ", Bill+(Quantity*220))
    elif option==6:
        print("The total bill of your food is -> ", pizza + dosa + punjabi + chinese + mexican )
        break
    else:
        print("Enter the valid option")
