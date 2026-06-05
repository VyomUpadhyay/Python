number = int(input("Enter the number u want to print the table of => "))
limit = int(input("Enter the limit => "))
i=number
while i<=limit:
    print( number, " X " , i , " = " , number*i)        
    i+=1