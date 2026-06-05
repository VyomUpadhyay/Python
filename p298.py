stocks = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}

while True:
    print("1 -> To Print The Data")
    print("2 -> To Add The Data")
    print("3 -> To Exit")

    operation = input("Enter operation =>  ")

    if operation == '1': 
        for k,v in stocks.items():
            print(k,v)

    elif operation == '2':  
        stock_ticker = input("Enter stock ticker: ")
        price = float(input("Enter price: ").strip())

        if stock_ticker in stocks:
            stocks[stock_ticker].append(price)
        else:
            stocks[stock_ticker] = [price]

        print(stock_ticker, "==>", stocks[stock_ticker], "added.")

    elif operation == '3':  
        break

    else:
        print("Invalid operation. Please try again.")
