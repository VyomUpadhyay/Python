#add 
#max2
def addtion():
    print("The addition of the two numbers is ", number1+number2)

def max():
    if number1>number2:
        print("Number 1 is greater than number 2")
    else:
        print("Number 2 is greater than number 1")

number1=int(input("Enter number 1 => "))
number2=int(input("Enter number 2 => "))

addtion(number1,number2)
max(number1,number2)