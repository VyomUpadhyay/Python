Character = str(input("Enter a letter to check wheather the letter uppercase or not => "))

if Character.isupper():
    print("Upper")
elif Character.islower():
    print("Lower")
else:
    print("Other")
    
