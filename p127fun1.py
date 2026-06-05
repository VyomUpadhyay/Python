def add():
    a=int(input("Enter no1 for addition =>"))
    b=int(input("Enter no2 for addition =>"))
    print("Add =",a+b)
       
def areaoftriangle():
    base = int(input("Enter the base of the triangle => "))
    height = int(input("Enter the height of the triangle => "))
    areaoftriangle = 0.5*base*height
    print(areaoftriangle)

def areaofcircle():
    radius = float(input("Enter the radius of the circle => "))
    circle = 2*(22/7)*radius
    print(circle)

def max():
    number1 = int(input("Enter number 1 to find minimum and maximum among these => "))
    number2 = int(input("Enter number 2 to find minimum and maximum among these => "))
    number3 = int(input("Enter number 3 to find minimum and maximum among these => "))

    if number1<number2:
        if number1<number3:
            print("The minimum number is ", number1)
        elif number2<number3:
            print("The minimum number is ",number2)
        else:
            print("The minimum number is ",number3)
    if number1>number2:
        if number1>number3:
            print("The maximum number is ", number1)
        elif number2>number3:
            print("The maximum number is ",number2)
        else:
            print("The maximum number is ",number3)

def table():
    number = int(input("Enter the number u want to print the table of => "))
    limit = int(input("Enter the limit => "))
    i=number
    while i<=limit:
        print( number, " X " , i , " = " , number*i)        
        i+=1
def factorials():
    number = int(input("Enter the number to find factorail of  => "))
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    print("The factorials is ", factorial)

def oddeven():
    number = int(input("Enter the number to check wheather it is odd or even => "))
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")

def positiveornegative():
    number = int(input("Enter the number to check wheather it is negative or positive => "))
    if number>0:
        print("Positive")
    elif number<0:
        print("Negative")
    else:
        print("The number is ZERO")


add()
areaoftriangle()
areaofcircle()
max()
table()
factorials()
oddeven()
positiveornegative()