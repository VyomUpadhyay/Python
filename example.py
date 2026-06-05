number = int(input("Enter the number you want to print the table of => "))

for i in range(1 , 71):
    if number%7==0:
        print(number*i)