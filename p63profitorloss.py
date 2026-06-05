BuyingPrice = int(input("Enter the Buying price of the product => "))
SellingPrice = int(input("Enter the Selling price of the product => "))

if SellingPrice>BuyingPrice:
    print("You have make profit of ", SellingPrice-BuyingPrice)
else:
    print("The total loss is ",BuyingPrice-SellingPrice)
    