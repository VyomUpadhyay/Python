num1 = int(input("Enter the first number => "))

if num1%3==0:
    print("FIZZ")
elif num1%5==0:
    print("BUZZ")
elif num1%3==0 and num1%5==0:
    print("FIZZ BUZZ")