number = int(input("Enter the number => "))
factorial = 1
while number > 1:
    factorial = factorial * number
    number = number - 1
print("The factorial is ",factorial)
