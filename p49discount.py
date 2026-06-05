MarkedPrice = int(input("Enter the marked price of the object => "))

if MarkedPrice>10000:   
    print("The final price will be = ", MarkedPrice-MarkedPrice*20/100 )

elif MarkedPrice>7000:
    print("The final price will be = ", MarkedPrice-MarkedPrice*15/100)
elif MarkedPrice<7000:
    print("The final price will be = " , MarkedPrice-MarkedPrice*10/100)
else:
    print("")